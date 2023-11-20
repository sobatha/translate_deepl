import deepl
from main import Settings

settings = Settings()

translator = deepl.Translator(settings.auth_key)

# Translate a formal document from English to German
input_path = "/path/to/Instruction Manual.docx"
output_path = "/path/to/Bedienungsanleitung.docx"
try:
    # Using translate_document_from_filepath() with file paths 
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="DE",
        formality="more"
    )

    # Alternatively you can use translate_document() with file IO objects
    with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
        translator.translate_document(
            in_file,
            out_file,
            target_lang="DE",
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
