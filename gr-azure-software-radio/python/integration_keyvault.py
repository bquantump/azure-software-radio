#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Microsoft Corporation.
# Licensed under the GNU General Public License v3.0 or later.
# See License.txt in the project root for license information.
#

import os
from gnuradio import gr_unittest
from azure_software_radio import keyvault
from azure_software_radio import default_credentials

keyvault_name = os.getenv('AZURE_KEYVAULT_NAME')
key_name = os.getenv('AZURE_KEYVAULT_TEST_KEY')
SECRET_VAL = "3.14"


class IntegrationKeyvault(gr_unittest.TestCase):
    """
    Integration tests for keyvault block.
    """

    def test_no_default_cred(self):
        """
        Test with no DefaultAzureCredential() supplied.
        """
        val = keyvault.pull_key(keyvault_name, key_name, '')
        self.assertEqual(val,SECRET_VAL, f"Val: {val}, SECRET_VAL: {SECRET_VAL} are not equal!")

    def test_default_cred_provided(self):
        """
        Test with DefaultAzureCredential() supplied.
        """
        dc = default_credentials.get_default_creds(enable_cli_credential=True,
                                                   enable_environment=True,
                                                   enable_managed_identity=True,
                                                   enable_powershell=True,
                                                   enable_visual_studio_code=True,
                                                   enable_shared_token_cache=True,
                                                   enable_interactive_browser=False)
        val = keyvault.pull_key(keyvault_name, key_name, dc)
        self.assertEqual(val,SECRET_VAL, f"Val: {val}, SECRET_VAL: {SECRET_VAL} are not equal!")


if __name__ == '__main__':
    gr_unittest.run(IntegrationKeyvault)
