# Regex to get CiviCRM ID from parentheses in contact name
# https://stackoverflow.com/a/38999572/1191545

import logging

import numpy as np
import pandas as pd
from django.core.exceptions import MultipleObjectsReturned
from django.core.management.base import BaseCommand
from tqdm import tqdm

from contact.models import (
    Meeting,
    MeetingWorshipTime,
    Organization,
)

logging.basicConfig(
    filename="civicrm_contact_import.log",
    level=logging.ERROR,
    format="%(message)s",
    # format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


def add_meeting_worship_times(meeting, contact):
    # For a given Meeting model instance,
    # add meeting time(s) from CiviCRM contact data

    if contact["Regular time of Worship on First Day (1)"] is not None:
        worship_time = MeetingWorshipTime(
            meeting=meeting,
            worship_type="first_day_worship",
            worship_time=contact["Regular time of Worship on First Day (1)"],
        )

        worship_time.save()

    if contact["Regular time of Worship on First Day (2)"] is not None:
        worship_time = MeetingWorshipTime(
            meeting=meeting,
            worship_type="first_day_worship_2nd",
            worship_time=contact["Regular time of Worship on First Day (2)"],
        )

        worship_time.save()

    if (
        contact[
            "Regular day and time of Meeting for Worship on the Occassion of Business"
        ]
        is not None
    ):
        worship_time = MeetingWorshipTime(
            meeting=meeting,
            worship_type="business_meeting",
            worship_time=contact[
                "Regular day and time of Meeting for Worship on the Occassion of Business"  # noqa: E501
            ],
        )

        worship_time.save()

    if (
        contact["Regular day and time of other weekly or monthly public meetings (1)"]
        is not None
    ):
        worship_time = MeetingWorshipTime(
            meeting=meeting,
            worship_type="other_regular_meeting",
            worship_time=contact[
                "Regular day and time of other weekly or monthly public meetings (1)"
            ],
        )

        worship_time.save()


def determine_meeting_type(contact_type):
    # Meeting Subtypes include
    # - Monthly_Meeting_Worship_Group
    # - Quarterly_Regional_Meeting
    # - Yearly_Meeting
    # - Worship_Group
    #
    # Each contact suptype is mapped
    # to a corresponding Meeting type

    meeting_types = {
        "Yearly_Meeting": "yearly_meeting",
        "Quarterly_Regional_Meeting": "quarterly_meeting",
        "Monthly_Meeting_Worship_Group": "monthly_meeting",
        "Worship_Group": "worship_group",
    }

    return meeting_types[contact_type]


class Command(BaseCommand):
    help = "Import Community Directory from Drupal site"

    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)

    def handle(self, *args, **options):
        contacts = (
            pd.read_csv(options["file"]).replace({np.nan: None}).to_dict("records")
        )

        for contact in tqdm(
            contacts,
            total=len(contacts),
            desc="Contacts",
            unit="row",
        ):
            # Check for entity type among:
            # - Meeting
            # - Organization
            #
            # Contact Subtypes include
            # - Monthly_Meeting_Worship_Group
            # - Quarterly_Regional_Meeting
            # - Yearly_Meeting
            # - Worship_Group
            # - Quaker_Organization
            # - NULL

            if contact["Contact Subtype"] is None:
                error_message = (
                    f"Contact { contact['Display Name']} does not have Contact Subtype"
                )
                logger.error(error_message)
                # Skip to next contact
                continue

            contact_type = contact["Contact Subtype"].strip()

            # Most of the contacts are meetings.
            # We will need nested logic to label the meeting based on type.
            meeting_types = [
                "Yearly_Meeting",
                "Quarterly_Regional_Meeting",
                "Monthly_Meeting_Worship_Group",
                "Worship_Group",
            ]

            # Organization types contains empty string
            # because contacts without a value
            # are organizations in the spreadsheet
            # Make sure empty string catches the contacts without subtype.
            organization_types = ["Quaker_Organization", ""]

            contact_is_meeting = contact_type in meeting_types
            contact_is_organization = contact_type in organization_types

            # Get common fields for use belos
            organization_name = contact["Organization Name"]
            civicrm_id = contact["Contact ID"]

            if contact_is_meeting:
                # Make sure we have exactly one record for this organization
                try:
                    meeting = Meeting.objects.get(
                        civicrm_id=civicrm_id,
                    )
                except MultipleObjectsReturned:
                    error_message = f"Duplicate contact found for {organization_name}"
                    logger.error(error_message)
                    continue
                except Meeting.DoesNotExist:
                    error_message = (
                        f"Could not find contact record for meeting {organization_name}"
                    )
                    logger.error(error_message)
                    continue

                # Update contact records with meeting data
                meeting.meeting_type = determine_meeting_type(contact_type)
                meeting.website = contact["Website"]
                meeting.phone = contact["Phone"]
                meeting.email = contact["Email"]

                meeting.save()

                add_meeting_worship_times(meeting, contact)
            elif contact_is_organization:
                # Make sure we have exactly one record for this organization
                try:
                    Organization.objects.get(
                        civicrm_id=civicrm_id,
                    )
                except MultipleObjectsReturned:
                    error_message = (
                        f"Duplicate contact records found for {organization_name}"
                    )
                    logger.error(error_message)
                    continue
                except Organization.DoesNotExist:
                    error_message = f"Could not find contact record for organization {organization_name}"  # noqa: E501
                    logger.error(error_message)
                    continue
            else:
                error_message = (
                    f"Invalid contact type '{contact_type} for {organization_name}"
                )
                logger.error(error_message)

        self.stdout.write("All done!")
