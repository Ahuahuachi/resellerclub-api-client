import unittest
import tests_settings as settings

from resellerclubapi import ResellerClubAPI


class TestDomainAvailability(unittest.TestCase):
    api = ResellerClubAPI(settings.RESELLER_ID, settings.API_KEY)
    single_domain = ["github"]
    single_tld = ["com"]
    multiple_domains = ["github", "google"]
    multiple_tlds = ["com", "net"]

    def test_single_domain_single_tld(self):
        domain_names = self.single_domain
        tlds = self.single_tld
        test_against = {
            "github.com": {"classkey": "domcno", "status": "regthroughothers"}
        }
        result = self.api.check_domain_availability(domain_names, tlds)

        self.assertDictContainsSubset(result, test_against)

    def test_single_domain_multiple_tlds(self):
        domain_names = self.single_domain
        tlds = self.multiple_tlds
        test_against = {
            "github.com": {"classkey": "domcno", "status": "regthroughothers"},
            "github.net": {"classkey": "dotnet", "status": "regthroughothers"},
        }
        result = self.api.check_domain_availability(domain_names, tlds)

        self.assertDictContainsSubset(result, test_against)

    def test_multiple_domains_single_tld(self):
        domain_names = self.multiple_domains
        tlds = self.single_tld
        test_against = {
            "github.com": {"classkey": "domcno", "status": "regthroughothers"},
            "google.com": {"classkey": "domcno", "status": "regthroughothers"},
        }
        result = self.api.check_domain_availability(domain_names, tlds)

        self.assertDictContainsSubset(result, test_against)

    def test_multiple_domains_multiple_tlds(self):
        domain_names = self.multiple_domains
        tlds = self.multiple_tlds
        test_against = {
            "google.com": {"classkey": "domcno", "status": "regthroughothers"},
            "github.net": {"classkey": "dotnet", "status": "regthroughothers"},
            "google.net": {"classkey": "dotnet", "status": "regthroughothers"},
            "github.com": {"classkey": "domcno", "status": "regthroughothers"},
        }
        result = self.api.check_domain_availability(domain_names, tlds)

        self.assertDictContainsSubset(result, test_against)