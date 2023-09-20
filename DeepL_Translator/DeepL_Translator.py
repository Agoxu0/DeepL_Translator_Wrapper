# DEEPL_Translator.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys

# All Language Tags.
language_tags = [
    # Bulgarian
    "bg",
    # Chinese (simplified)
    "zh",
    # Czech
    "cs",
    # Danish
    "da",
    # Dutch
    "nl",
    # English (American)
    "en-US",
    # English (British)
    "en-GB",
    # Estonian
    "et",
    # Finnish
    "fi",
    # French
    "fr",
    # German
    "de",
    # Greek
    "el",
    # Hungarian
    "hu",
    # Indonesian
    "id",
    # Italian
    "it",
    # Japanese
    "ja",
    # Korean
    "ko",
    # Latvian
    "lv",
    # Lithuanian
    "lt",
    # Norwegian (bokmål)
    "nb",
    # Polish
    "pl",
    # Portuguese
    "pt-PT",
    # Portuguese (Brazilian)
    "pt-BR",
    # Romanian
    "ro",
    # Russian
    "ru",
    # Slovak
    "sk",
    # Slovenian
    "sl",
    # Spanish
    "es",
    # Swedish
    "sv",
    # Turkish
    "tr",
    # Ukrainian
    "uk"
]

class DEEPL_Translator:
    '''
    Unofficial Wrapper For DEEPL Translator.
    '''
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1024,768')
        options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.deepl.com/translator")

        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def Translate(self, text, target_language):
        '''
        Translate the given text to the target language.

        Args:
        text (str): The text you want to translate.
        target_language (str): The target language code (e.g., "pl" for Polish, "en_GB" for British English).

        Returns:
        str: The translated text.
        
        Raises:
        ValueError: If the target_language is not supported.
        NoSuchElementException: If an element is not found on the page.
        '''
        if not target_language in language_tags:
            raise ValueError('No Such Language!/Not Supported Language!')

        try:
            translate_textbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '(//div[@role="textbox"])'))
            )
            translate_textbox.click()
            translate_textbox.send_keys(text)

            translation_target_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '(//button[@data-testid="translator-target-lang-btn"])'))
            )
            self.driver.execute_script("arguments[0].click();", translation_target_button)

            languagetoselect = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//button[@data-testid="translator-lang-option-{target_language}"]'))
            )
            self.driver.execute_script("arguments[0].click();", languagetoselect)
            
            translation_textbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '(//div[@role="textbox"])[2]'))
            )

            while True:
                if not translation_textbox.text == '':
                    break

            translation = translation_textbox.text
            translate_textbox.clear()
        except NoSuchElementException:
            sys.exit('Language selection element not found.')

        return translation

    def __del__(self):
        self.driver.quit()