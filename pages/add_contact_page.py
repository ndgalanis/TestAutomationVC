from pages.page_utils.base_page import BasePage
from pages.page_utils.page_constants import PageConstants

class AddContactPage(BasePage):
    """
    AddContactPage page object representing the "Add Contact" page.
    Inherits from BasePage and provides methods to interact with the contact form.
    """

    def __init__(self):
        """
        Initializes the AddContactPage page with a predefined URL and title.
        """
        super().__init__()
        self.url = f'{PageConstants.BASE_URL}/addContact'
        self.title = 'Add Contact'

    def get_page_title(self):
        """
        Returns the XPath expression for verifying the page title.

        :return: XPath string for the page title.
        """
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_first_name_field():
        """
        Returns the XPath for the first name input field.

        :return: XPath string for the first name field.
        """
        return '//Input[@id="firstName"]'

    @staticmethod
    def get_path_last_name_field():
        """
        Returns the XPath for the last name input field.

        :return: XPath string for the last name field.
        """
        return '//Input[@id="lastName"]'

    @staticmethod
    def get_path_birthdate_field():
        """
        Returns the XPath for the birthdate input field.

        :return: XPath string for the birthdate field.
        """
        return '//input[@id="birthdate"]'

    @staticmethod
    def get_path_birthdate_error():
        """
        Returns the XPath for the birthdate validation error message.

        :return: XPath string for the birthdate error message.
        """
        return "//span[@id='error' and contains(text(), 'Birthdate is invalid')]"

    @staticmethod
    def get_path_submit_button():
        """
        Returns the XPath for the submit button.

        :return: XPath string for the submit button.
        """
        return '//button[@id="submit"]'

    def enter_birthdate(self, birthdate: str or int):
        """
        Enters text into the birthdate input field.

        :param birthdate: The birthdate to enter.
        """
        self.enter_text(self.get_path_birthdate_field(), birthdate)

    def enter_first_name(self, first_name: str):
        """
        Enters text into the first name input field.

        :param first_name: The first name to enter.
        """
        self.enter_text(self.get_path_first_name_field(), first_name)

    def enter_last_name(self, last_name: str):
        """
        Enters text into the last name input field.

        :param last_name: The last name to enter.
        """
        self.enter_text(self.get_path_last_name_field(), last_name)

    def check_birthdate_error_exists(self):
        """
        Checks if the birthdate validation error message is displayed.

        :return: True if the error message is found, otherwise raises an exception.
        """
        self.element_exists(self.get_path_birthdate_error())

    def click_submit_button(self):
        """
        Clicks the submit button to submit the form and returns an object of the landing page which is the
        ContactList page.

        :return: An instance of the ContactList page object.
        """
        self.click_element(self.get_path_submit_button())
        from pages.contact_list_page import ContactListPage
        return ContactListPage()

    def check_title(self):
        """
        Verifies that the "Add Contact" page title is displayed.

        :return: True if the title is found, otherwise raises an exception.
        """
        self.element_exists(self.get_page_title())
