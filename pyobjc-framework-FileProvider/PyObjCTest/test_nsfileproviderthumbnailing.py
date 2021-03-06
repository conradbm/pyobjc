import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderThumbnailing(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.fetchThumbnailsForItemIdentifiers_requestedSize_perThumbnailCompletionHandler_completionHandler_,  # noqa: B950
            3,
            b"v@",
        )
