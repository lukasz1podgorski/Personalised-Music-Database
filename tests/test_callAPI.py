import pytest
import callAPI as callAPI
import unittest.mock as mock


@mock.patch("callAPI.get_token")
def test_get_token(mock_get_token):
    mock_get_token.return_value = "BQCnYFGFQM8nkY8DQzjgUShVv3OpnwqGjI319BLzz_hDCJKfFcuPxV4" \
                                  "--Tkv4rJzz3p1F5rFiDsCcm_hlDjRBXYR22_jjqRUuLie_AnsI9EmInlyJPo"
    token = callAPI.get_token()

    assert token == "BQCnYFGFQM8nkY8DQzjgUShVv3OpnwqGjI319BLzz_hDCJKfFcuPxV4" \
                    "--Tkv4rJzz3p1F5rFiDsCcm_hlDjRBXYR22_jjqRUuLie_AnsI9EmInlyJPo"


@mock.patch("callAPI.search_for_new_releases")
def test_search_for_new_releases(mock_search_for_new_releases):

    mock_search_for_new_releases.return_value = {"name": "Izzy and the Black Trees", "release_date": "2024-04-05"}
    data = callAPI.search_for_new_releases(access_token="BQCnYFGFQM8nkY8DQzjgUShVv3OpnwqGjI319BLzz_hDCJKfFcuPxV4" \
                                                        "--Tkv4rJzz3p1F5rFiDsCcm_hlDjRBXYR22_jjqRUuLie_AnsI9EmInlyJPo", country="PL")
    assert data == {"name": "Izzy and the Black Trees", "release_date": "2024-04-05"}
