# This test script was automatically generated by the contrib-patch-tests.py
# script. If you want to make changes to it, you should make sure that you have
# removed the ``_generated`` suffix from the file name, to prevent the content
# from being overwritten by future re-generations.

from ddtrace.contrib.internal.openai.patch import OPENAI_VERSION
from ddtrace.contrib.internal.openai.patch import get_version
from ddtrace.contrib.internal.openai.patch import patch
from ddtrace.contrib.internal.openai.patch import unpatch
from tests.contrib.patch import PatchTestCase


class TestOpenaiPatch(PatchTestCase.Base):
    __integration_name__ = "openai"
    __module_name__ = "openai"
    __patch_func__ = patch
    __unpatch_func__ = unpatch
    __get_version__ = get_version

    def assert_module_patched(self, openai):
        if OPENAI_VERSION >= (1, 0, 0):
            if OPENAI_VERSION >= (1, 8, 0):
                self.assert_wrapped(openai._base_client.SyncAPIClient._process_response)
                self.assert_wrapped(openai._base_client.AsyncAPIClient._process_response)
            else:
                self.assert_wrapped(openai._base_client.BaseClient._process_response)
            self.assert_wrapped(openai.OpenAI.__init__)
            self.assert_wrapped(openai.AsyncOpenAI.__init__)
            self.assert_wrapped(openai.AzureOpenAI.__init__)
            self.assert_wrapped(openai.AsyncAzureOpenAI.__init__)
            self.assert_wrapped(openai.resources.models.Models.list)
            self.assert_wrapped(openai.resources.models.Models.retrieve)
            self.assert_wrapped(openai.resources.models.Models.delete)
            self.assert_wrapped(openai.resources.models.AsyncModels.list)
            self.assert_wrapped(openai.resources.models.AsyncModels.retrieve)
            self.assert_wrapped(openai.resources.models.AsyncModels.delete)
            self.assert_wrapped(openai.resources.completions.Completions.create)
            self.assert_wrapped(openai.resources.chat.Completions.create)
            self.assert_wrapped(openai.resources.completions.AsyncCompletions.create)
            self.assert_wrapped(openai.resources.chat.AsyncCompletions.create)
            self.assert_wrapped(openai.resources.images.Images.generate)
            self.assert_wrapped(openai.resources.images.Images.edit)
            self.assert_wrapped(openai.resources.images.Images.create_variation)
            self.assert_wrapped(openai.resources.images.AsyncImages.generate)
            self.assert_wrapped(openai.resources.images.AsyncImages.edit)
            self.assert_wrapped(openai.resources.images.AsyncImages.create_variation)
            self.assert_wrapped(openai.resources.audio.Transcriptions.create)
            self.assert_wrapped(openai.resources.audio.Translations.create)
            self.assert_wrapped(openai.resources.audio.AsyncTranscriptions.create)
            self.assert_wrapped(openai.resources.audio.AsyncTranslations.create)
            self.assert_wrapped(openai.resources.embeddings.Embeddings.create)
            self.assert_wrapped(openai.resources.moderations.Moderations.create)
            self.assert_wrapped(openai.resources.embeddings.AsyncEmbeddings.create)
            self.assert_wrapped(openai.resources.moderations.AsyncModerations.create)
            self.assert_wrapped(openai.resources.files.Files.create)
            self.assert_wrapped(openai.resources.files.Files.retrieve)
            self.assert_wrapped(openai.resources.files.Files.list)
            self.assert_wrapped(openai.resources.files.Files.delete)
            self.assert_wrapped(openai.resources.files.Files.retrieve_content)
            self.assert_wrapped(openai.resources.files.AsyncFiles.create)
            self.assert_wrapped(openai.resources.files.AsyncFiles.retrieve)
            self.assert_wrapped(openai.resources.files.AsyncFiles.list)
            self.assert_wrapped(openai.resources.files.AsyncFiles.delete)
            self.assert_wrapped(openai.resources.files.AsyncFiles.retrieve_content)
        else:
            self.assert_wrapped(openai.api_resources.completion.Completion.create)
            self.assert_wrapped(openai.api_resources.completion.Completion.acreate)
            self.assert_wrapped(openai.api_requestor._make_session)
            self.assert_wrapped(openai.util.convert_to_openai_object)
            self.assert_wrapped(openai.api_resources.embedding.Embedding.create)
            self.assert_wrapped(openai.api_resources.embedding.Embedding.acreate)
            if hasattr(openai, "Model"):
                self.assert_wrapped(openai.api_resources.model.Model.list)
                self.assert_wrapped(openai.api_resources.model.Model.retrieve)
                self.assert_wrapped(openai.api_resources.model.Model.delete)
                self.assert_wrapped(openai.api_resources.model.Model.alist)
                self.assert_wrapped(openai.api_resources.model.Model.aretrieve)
                self.assert_wrapped(openai.api_resources.model.Model.adelete)
            if hasattr(openai, "ChatCompletion"):
                self.assert_wrapped(openai.api_resources.chat_completion.ChatCompletion.create)
                self.assert_wrapped(openai.api_resources.chat_completion.ChatCompletion.acreate)
            if hasattr(openai, "Image"):
                self.assert_wrapped(openai.api_resources.image.Image.create)
                self.assert_wrapped(openai.api_resources.image.Image.acreate)
                self.assert_wrapped(openai.api_resources.image.Image.create_edit)
                self.assert_wrapped(openai.api_resources.image.Image.acreate_edit)
                self.assert_wrapped(openai.api_resources.image.Image.create_variation)
                self.assert_wrapped(openai.api_resources.image.Image.acreate_variation)
            if hasattr(openai, "Audio"):
                self.assert_wrapped(openai.api_resources.audio.Audio.transcribe)
                self.assert_wrapped(openai.api_resources.audio.Audio.atranscribe)
                self.assert_wrapped(openai.api_resources.audio.Audio.translate)
                self.assert_wrapped(openai.api_resources.audio.Audio.atranslate)
            if hasattr(openai, "Moderation"):
                self.assert_wrapped(openai.api_resources.moderation.Moderation.create)
                self.assert_wrapped(openai.api_resources.moderation.Moderation.acreate)
            if hasattr(openai, "File"):
                self.assert_wrapped(openai.api_resources.file.File.create)
                self.assert_wrapped(openai.api_resources.file.File.retrieve)
                self.assert_wrapped(openai.api_resources.file.File.list)
                self.assert_wrapped(openai.api_resources.file.File.delete)
                self.assert_wrapped(openai.api_resources.file.File.download)
                self.assert_wrapped(openai.api_resources.file.File.acreate)
                self.assert_wrapped(openai.api_resources.file.File.aretrieve)
                self.assert_wrapped(openai.api_resources.file.File.alist)
                self.assert_wrapped(openai.api_resources.file.File.adelete)
                self.assert_wrapped(openai.api_resources.file.File.adownload)

    def assert_not_module_patched(self, openai):
        if OPENAI_VERSION >= (1, 0, 0):
            if OPENAI_VERSION >= (1, 8, 0):
                self.assert_not_wrapped(openai._base_client.SyncAPIClient._process_response)
                self.assert_not_wrapped(openai._base_client.AsyncAPIClient._process_response)
            else:
                self.assert_not_wrapped(openai._base_client.BaseClient._process_response)
            self.assert_not_wrapped(openai.OpenAI.__init__)
            self.assert_not_wrapped(openai.AsyncOpenAI.__init__)
            self.assert_not_wrapped(openai.AzureOpenAI.__init__)
            self.assert_not_wrapped(openai.AsyncAzureOpenAI.__init__)
            self.assert_not_wrapped(openai.resources.models.Models.list)
            self.assert_not_wrapped(openai.resources.models.Models.retrieve)
            self.assert_not_wrapped(openai.resources.models.Models.delete)
            self.assert_not_wrapped(openai.resources.models.AsyncModels.list)
            self.assert_not_wrapped(openai.resources.models.AsyncModels.retrieve)
            self.assert_not_wrapped(openai.resources.models.AsyncModels.delete)
            self.assert_not_wrapped(openai.resources.completions.Completions.create)
            self.assert_not_wrapped(openai.resources.chat.Completions.create)
            self.assert_not_wrapped(openai.resources.completions.AsyncCompletions.create)
            self.assert_not_wrapped(openai.resources.chat.AsyncCompletions.create)
            self.assert_not_wrapped(openai.resources.images.Images.generate)
            self.assert_not_wrapped(openai.resources.images.Images.edit)
            self.assert_not_wrapped(openai.resources.images.Images.create_variation)
            self.assert_not_wrapped(openai.resources.images.AsyncImages.generate)
            self.assert_not_wrapped(openai.resources.images.AsyncImages.edit)
            self.assert_not_wrapped(openai.resources.images.AsyncImages.create_variation)
            self.assert_not_wrapped(openai.resources.audio.Transcriptions.create)
            self.assert_not_wrapped(openai.resources.audio.Translations.create)
            self.assert_not_wrapped(openai.resources.audio.AsyncTranscriptions.create)
            self.assert_not_wrapped(openai.resources.audio.AsyncTranslations.create)
            self.assert_not_wrapped(openai.resources.embeddings.Embeddings.create)
            self.assert_not_wrapped(openai.resources.moderations.Moderations.create)
            self.assert_not_wrapped(openai.resources.embeddings.AsyncEmbeddings.create)
            self.assert_not_wrapped(openai.resources.moderations.AsyncModerations.create)
            self.assert_not_wrapped(openai.resources.files.Files.create)
            self.assert_not_wrapped(openai.resources.files.Files.retrieve)
            self.assert_not_wrapped(openai.resources.files.Files.list)
            self.assert_not_wrapped(openai.resources.files.Files.delete)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.retrieve_content)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.create)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.retrieve)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.list)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.delete)
            self.assert_not_wrapped(openai.resources.files.AsyncFiles.retrieve_content)
        else:
            self.assert_not_wrapped(openai.api_resources.completion.Completion.create)
            self.assert_not_wrapped(openai.api_resources.completion.Completion.acreate)
            self.assert_not_wrapped(openai.api_requestor._make_session)
            self.assert_not_wrapped(openai.util.convert_to_openai_object)
            self.assert_not_wrapped(openai.api_resources.embedding.Embedding.create)
            self.assert_not_wrapped(openai.api_resources.embedding.Embedding.acreate)
            if hasattr(openai, "Model"):
                self.assert_not_wrapped(openai.api_resources.model.Model.list)
                self.assert_not_wrapped(openai.api_resources.model.Model.retrieve)
                self.assert_not_wrapped(openai.api_resources.model.Model.delete)
                self.assert_not_wrapped(openai.api_resources.model.Model.alist)
                self.assert_not_wrapped(openai.api_resources.model.Model.aretrieve)
                self.assert_not_wrapped(openai.api_resources.model.Model.adelete)
            if hasattr(openai, "ChatCompletion"):
                self.assert_not_wrapped(openai.api_resources.chat_completion.ChatCompletion.create)
                self.assert_not_wrapped(openai.api_resources.chat_completion.ChatCompletion.acreate)
            if hasattr(openai, "Image"):
                self.assert_not_wrapped(openai.api_resources.image.Image.create)
                self.assert_not_wrapped(openai.api_resources.image.Image.acreate)
                self.assert_not_wrapped(openai.api_resources.image.Image.create_edit)
                self.assert_not_wrapped(openai.api_resources.image.Image.acreate_edit)
                self.assert_not_wrapped(openai.api_resources.image.Image.create_variation)
                self.assert_not_wrapped(openai.api_resources.image.Image.acreate_variation)
            if hasattr(openai, "Audio"):
                self.assert_not_wrapped(openai.api_resources.audio.Audio.transcribe)
                self.assert_not_wrapped(openai.api_resources.audio.Audio.atranscribe)
                self.assert_not_wrapped(openai.api_resources.audio.Audio.translate)
                self.assert_not_wrapped(openai.api_resources.audio.Audio.atranslate)
            if hasattr(openai, "Moderation"):
                self.assert_not_wrapped(openai.api_resources.moderation.Moderation.create)
                self.assert_not_wrapped(openai.api_resources.moderation.Moderation.acreate)
            if hasattr(openai, "File"):
                self.assert_not_wrapped(openai.api_resources.file.File.create)
                self.assert_not_wrapped(openai.api_resources.file.File.retrieve)
                self.assert_not_wrapped(openai.api_resources.file.File.list)
                self.assert_not_wrapped(openai.api_resources.file.File.delete)
                self.assert_not_wrapped(openai.api_resources.file.File.download)
                self.assert_not_wrapped(openai.api_resources.file.File.acreate)
                self.assert_not_wrapped(openai.api_resources.file.File.aretrieve)
                self.assert_not_wrapped(openai.api_resources.file.File.alist)
                self.assert_not_wrapped(openai.api_resources.file.File.adelete)
                self.assert_not_wrapped(openai.api_resources.file.File.adownload)

    def assert_not_module_double_patched(self, openai):
        if OPENAI_VERSION >= (1, 0, 0):
            if OPENAI_VERSION >= (1, 8, 0):
                self.assert_not_double_wrapped(openai._base_client.SyncAPIClient._process_response)
                self.assert_not_double_wrapped(openai._base_client.AsyncAPIClient._process_response)
            else:
                self.assert_not_double_wrapped(openai._base_client.BaseClient._process_response)
            self.assert_not_double_wrapped(openai.OpenAI.__init__)
            self.assert_not_double_wrapped(openai.AsyncOpenAI.__init__)
            self.assert_not_double_wrapped(openai.AzureOpenAI.__init__)
            self.assert_not_double_wrapped(openai.AsyncAzureOpenAI.__init__)
            self.assert_not_double_wrapped(openai.resources.models.Models.list)
            self.assert_not_double_wrapped(openai.resources.models.Models.retrieve)
            self.assert_not_double_wrapped(openai.resources.models.Models.delete)
            self.assert_not_double_wrapped(openai.resources.models.AsyncModels.list)
            self.assert_not_double_wrapped(openai.resources.models.AsyncModels.retrieve)
            self.assert_not_double_wrapped(openai.resources.models.AsyncModels.delete)
            self.assert_not_double_wrapped(openai.resources.completions.Completions.create)
            self.assert_not_double_wrapped(openai.resources.chat.Completions.create)
            self.assert_not_double_wrapped(openai.resources.completions.AsyncCompletions.create)
            self.assert_not_double_wrapped(openai.resources.chat.AsyncCompletions.create)
            self.assert_not_double_wrapped(openai.resources.images.Images.generate)
            self.assert_not_double_wrapped(openai.resources.images.Images.edit)
            self.assert_not_double_wrapped(openai.resources.images.Images.create_variation)
            self.assert_not_double_wrapped(openai.resources.images.AsyncImages.generate)
            self.assert_not_double_wrapped(openai.resources.images.AsyncImages.edit)
            self.assert_not_double_wrapped(openai.resources.images.AsyncImages.create_variation)
            self.assert_not_double_wrapped(openai.resources.audio.Transcriptions.create)
            self.assert_not_double_wrapped(openai.resources.audio.Translations.create)
            self.assert_not_double_wrapped(openai.resources.audio.AsyncTranscriptions.create)
            self.assert_not_double_wrapped(openai.resources.audio.AsyncTranslations.create)
            self.assert_not_double_wrapped(openai.resources.embeddings.Embeddings.create)
            self.assert_not_double_wrapped(openai.resources.moderations.Moderations.create)
            self.assert_not_double_wrapped(openai.resources.embeddings.AsyncEmbeddings.create)
            self.assert_not_double_wrapped(openai.resources.moderations.AsyncModerations.create)
            self.assert_not_double_wrapped(openai.resources.files.Files.create)
            self.assert_not_double_wrapped(openai.resources.files.Files.retrieve)
            self.assert_not_double_wrapped(openai.resources.files.Files.list)
            self.assert_not_double_wrapped(openai.resources.files.Files.delete)
            self.assert_not_double_wrapped(openai.resources.files.Files.retrieve_content)
            self.assert_not_double_wrapped(openai.resources.files.AsyncFiles.create)
            self.assert_not_double_wrapped(openai.resources.files.AsyncFiles.retrieve)
            self.assert_not_double_wrapped(openai.resources.files.AsyncFiles.list)
            self.assert_not_double_wrapped(openai.resources.files.AsyncFiles.delete)
            self.assert_not_double_wrapped(openai.resources.files.AsyncFiles.retrieve_content)
        else:
            self.assert_not_double_wrapped(openai.api_resources.completion.Completion.create)
            self.assert_not_double_wrapped(openai.api_resources.completion.Completion.acreate)
            self.assert_not_double_wrapped(openai.api_requestor._make_session)
            self.assert_not_double_wrapped(openai.util.convert_to_openai_object)
            self.assert_not_double_wrapped(openai.api_resources.embedding.Embedding.create)
            self.assert_not_double_wrapped(openai.api_resources.embedding.Embedding.acreate)
            if hasattr(openai, "Model"):
                self.assert_not_double_wrapped(openai.api_resources.model.Model.list)
                self.assert_not_double_wrapped(openai.api_resources.model.Model.retrieve)
                self.assert_not_double_wrapped(openai.api_resources.model.Model.delete)
                self.assert_not_double_wrapped(openai.api_resources.model.Model.alist)
                self.assert_not_double_wrapped(openai.api_resources.model.Model.aretrieve)
                self.assert_not_double_wrapped(openai.api_resources.model.Model.adelete)
            if hasattr(openai, "ChatCompletion"):
                self.assert_not_double_wrapped(openai.api_resources.chat_completion.ChatCompletion.create)
                self.assert_not_double_wrapped(openai.api_resources.chat_completion.ChatCompletion.acreate)
            if hasattr(openai, "Image"):
                self.assert_not_double_wrapped(openai.api_resources.image.Image.create)
                self.assert_not_double_wrapped(openai.api_resources.image.Image.acreate)
                self.assert_not_double_wrapped(openai.api_resources.image.Image.create_edit)
                self.assert_not_double_wrapped(openai.api_resources.image.Image.acreate_edit)
                self.assert_not_double_wrapped(openai.api_resources.image.Image.create_variation)
                self.assert_not_double_wrapped(openai.api_resources.image.Image.acreate_variation)
            if hasattr(openai, "Audio"):
                self.assert_not_double_wrapped(openai.api_resources.audio.Audio.transcribe)
                self.assert_not_double_wrapped(openai.api_resources.audio.Audio.atranscribe)
                self.assert_not_double_wrapped(openai.api_resources.audio.Audio.translate)
                self.assert_not_double_wrapped(openai.api_resources.audio.Audio.atranslate)
            if hasattr(openai, "Moderation"):
                self.assert_not_double_wrapped(openai.api_resources.moderation.Moderation.create)
                self.assert_not_double_wrapped(openai.api_resources.moderation.Moderation.acreate)
            if hasattr(openai, "File"):
                self.assert_not_double_wrapped(openai.api_resources.file.File.create)
                self.assert_not_double_wrapped(openai.api_resources.file.File.retrieve)
                self.assert_not_double_wrapped(openai.api_resources.file.File.list)
                self.assert_not_double_wrapped(openai.api_resources.file.File.delete)
                self.assert_not_double_wrapped(openai.api_resources.file.File.download)
                self.assert_not_double_wrapped(openai.api_resources.file.File.acreate)
                self.assert_not_double_wrapped(openai.api_resources.file.File.aretrieve)
                self.assert_not_double_wrapped(openai.api_resources.file.File.alist)
                self.assert_not_double_wrapped(openai.api_resources.file.File.adelete)
                self.assert_not_double_wrapped(openai.api_resources.file.File.adownload)
