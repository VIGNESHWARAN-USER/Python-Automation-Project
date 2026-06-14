from pages.super_admin_page import superadmin
from actions.base_action import BaseAction
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
import pytest

logger = get_logger()
class Superadminaction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.sap = superadmin()
        self.side = SideBarPage()

    def opd(self):
        try:
            self.click(self.sap.opd)
            self.click(self.sap.upcimopd)
            self.click(self.sap.oldopd)
            self.click(self.sap.opdpatientview)

            return self.is_displayed(self.sap.opdpatientview)

        except Exception as e:
            self.take_screenshot("opd_failure")
            pytest.fail(f"Unable to complete OPD operation. Error: {str(e)}")

    def ipd(self):
        try:
            self.click(self.sap.ipd)
            return self.is_displayed(self.sap.patientlistipd)

        except Exception as e:
            self.take_screenshot("ipd_failure")
            pytest.fail(f"Unable to complete IPD operation. Error: {str(e)}")

    def medicine_details(self,medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note,):
        try:
            self.wait_for_visibility(self.sap.pharmacy)
            self.js_click(self.sap.pharmacy)
            self.wait_for_visibility(self.sap.addmed)
            self.js_click(self.sap.addmed)
            self.wait_for_visibility(self.sap.medname)
            self.send_keys(self.sap.medname, medicalname)
            self.wait_for_visibility(self.sap.medgroup)
            self.select_by_index(self.sap.medgroup, 1)
            self.wait_for_visibility(self.sap.unit)
            self.select_by_index(self.sap.unit, 1)
            self.wait_for_visibility(self.sap.medcompany)
            self.select_by_index(self.sap.medcompany, 1)
            self.wait_for_visibility(self.sap.medcompos)
            self.send_keys(self.sap.medcompos, composition)
            self.wait_for_visibility(self.sap.minlvl)
            self.send_keys(self.sap.minlvl, minlevel)
            self.wait_for_visibility(self.sap.reorder)
            self.send_keys(self.sap.reorder, reorderlevel)
            self.wait_for_visibility(self.sap.tax)
            self.send_keys(self.sap.tax, tax)
            self.wait_for_visibility(self.sap.vatac)
            self.send_keys(self.sap.vatac, vatac)
            self.wait_for_visibility(self.sap.racknum)
            self.send_keys(self.sap.racknum, racknumber)
            self.wait_for_visibility(self.sap.box)
            self.send_keys(self.sap.box, boxpacking)
            self.wait_for_visibility(self.sap.note)
            self.send_keys(self.sap.note, note)
            self.wait_for_visibility(self.sap.savebtn)
            self.click(self.sap.savebtn)
            self.wait_for_visibility(self.sap.medicinestock)
            return self.is_displayed(self.sap.medicinestock)

        except Exception as e:
            self.take_screenshot("pharmacy_failure")
            pytest.fail(f"Unable to add medicine details. Error: {str(e)}")

    def pathology(self):
        try:
            self.js_click(self.sap.pathology)
            self.js_click(self.sap.pathologytest)
            return self.is_displayed(self.sap.testlist)

        except Exception as e:
            self.take_screenshot("pathology_failure")
            pytest.fail(f"Unable to open Pathology module. Error: {str(e)}")

    def radiology(self):
        try:
            self.js_click(self.sap.radiology)
            return self.is_displayed(self.sap.radiologytestlist)

        except Exception as e:
            self.take_screenshot("radiology_failure")
            pytest.fail(f"Unable to open Radiology module. Error: {str(e)}")

    def bloodbank(self):
        try:
            self.js_click(self.sap.bloodbank)
            self.js_click(self.sap.status)
            self.click(self.sap.donordet)
            self.click(self.sap.issuedet)

            return self.is_displayed(self.sap.component)

        except Exception as e:
            self.take_screenshot("bloodbank_failure")
            pytest.fail(f"Unable to open Blood Bank module. Error: {str(e)}")

    def ambulance(self):
        try:
            self.scroll_and_click(self.sap.ambulance)
            self.js_click(self.sap.ambulancelist)
            return self.is_displayed(self.sap.calllist)

        except Exception as e:
            self.take_screenshot("ambulance_failure")
            pytest.fail(f"Unable to open Ambulance module. Error: {str(e)}")

    def general(self):
        try:
            self.scroll_and_click(self.sap.generalinc)
            return self.is_displayed(self.sap.incomelist)

        except Exception as e:
            self.take_screenshot("general_income_failure")
            pytest.fail(f"Unable to open General Income module. Error: {str(e)}")

    def expenses(self):
        try:
            self.js_click(self.sap.expenses)
            return self.is_displayed(self.sap.expenselist)

        except Exception as e:
            self.take_screenshot("expense_failure")
            pytest.fail(f"Unable to open Expense module. Error: {str(e)}")
