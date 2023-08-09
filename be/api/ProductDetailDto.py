from googletrans import Translator
import constants

class ProductDto:
    def __init__(self, title, product_url, main_imgs, product_props, sku_props, skus):
        self._title = title
        self._product_url = product_url
        self._main_imgs = main_imgs
        self._product_props = product_props
        self._sku_props = sku_props
        self._skus = skus
        # Translate text using your translation API

    def translate_text(self, text, target_language):
        translator = Translator()
        # Replace this with the actual code to make the API request
        translation = translator.translate(text, src=constants.CHINESE, dest=target_language)
        return translation

    def translate(self, target_language):
        self._title = self.translate_text(self._title, target_language)
        # self._product_props = [self.translate_text(prop, target_language) for prop in self._product_props]
        # self._sku_props = [self.translate_text(prop, target_language) for prop in self._sku_props]

    # Getter methods with translation
    def get_title(self, target_language):
        return self.translate_text(self._title, target_language)

    def get_main_imgs(self):
        return self._main_imgs

    def get_product_props(self, target_language):
        return [self.translate_text(prop, target_language) for prop in self._product_props]

    def get_sku_props(self, target_language):
        return [self.translate_text(prop, target_language) for prop in self._sku_props]

    def get_skus(self):
        return self._skus

    def get_product_url(self):
        return self._product_url

    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_main_imgs(self, main_imgs):
        self._main_imgs = main_imgs

    def set_product_props(self, product_props):
        self._product_props = product_props

    def set_sku_props(self, sku_props):
        self._sku_props = sku_props

    def set_skus(self, skus):
        self._skus = skus

    def set_product_url(self, product_url):
        self._product_url = product_url