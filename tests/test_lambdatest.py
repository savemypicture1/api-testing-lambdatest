import allure
import pytest
from utils.file_utils import read_data_file


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-xml-converter")
@allure.title("JSON to XML conversion")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_xml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        mini_expected_xml = lambdatest_service.minify_xml(expected_xml)

    with allure.step("Convert JSON to XML via API"):
        actual_xml = lambdatest_service.json_to_xml(input_json)
        mini_actual_xml = lambdatest_service.minify_xml(actual_xml)

    with allure.step("Compare expected and actual XML"):
        assert mini_actual_xml == mini_expected_xml


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.title("Extract text from JSON")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-text")
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected and actual text.
""")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_extract_text_from_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_text = read_data_file(f"txt/{file_name}.txt")

    with allure.step("Extract text from JSON via API"):
        actual_text = lambdatest_service.extract_text_from_json(input_json)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Lambdatest API tests")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@allure.title("YAML validation test")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_validator(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Validation YAML via API"):
        response = lambdatest_service.yaml_validator(input_yaml)

    with allure.step("Compare expected and actual text"):
        assert response == "Valid YAML"


@allure.suite("Lambdatest API tests")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@allure.title("YAML validation test")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Convert JSON to YAML via API"):
        actual_yaml = lambdatest_service.json_to_yaml(input_json)

    with allure.step("Compare expected and actual text"):
        assert actual_yaml == f"{expected_yaml}\n"


@allure.suite("Lambdatest API tests")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml")
@allure.title("XML to YAML conversion")
@pytest.mark.xfail(reason="Bug in the API")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_xml_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        expected_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Convert XML to YAML via API"):
        actual_yaml = lambdatest_service.xml_to_yaml(input_xml)

    with allure.step("Compare expected and actual text"):
        assert actual_yaml == f"{expected_yaml}\n"


@allure.suite("Lambdatest API tests")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-to-json")
@allure.title("YAML to JSON conversion")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_to_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yml")
        expected_json = read_data_file(f"json/{file_name}.json")

    with allure.step("Convert YAML to JSON via API"):
        actual_json = lambdatest_service.yaml_to_json(input_yaml)

    with allure.step("Compare expected and actual text"):
        assert actual_json.replace(' ', '') == expected_json.replace('\n', '').replace(' ', '')
