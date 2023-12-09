import deepl
from app import config


settings = config.Settings()

items = settings.items_per_user


def translate_test_file():
    input_path = "app/translate_results/test_input.txt"
    output_path = "app/translate_results/test_output.txt"
    try:
        # Alternatively you can use translate_document() with file IO objects
        with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
            print(items)
            translator = deepl.Translator(settings.auth_key)
            translator.translate_document(
                in_file,
                out_file,
                target_lang="JA",
                formality="more"
            )

    except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        print(error)
