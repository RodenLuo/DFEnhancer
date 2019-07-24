from chimerax.core.toolshed import BundleAPI

class _SeggerAPI(BundleAPI):
    @staticmethod
    def initialize(session, bundle_info):
        """Register file formats, commands, and database fetch."""
        from .segfile import register_segmentation_file_format
        register_segmentation_file_format(session)

    @staticmethod
    def start_tool(session, tool_name):
        if tool_name == 'Segment Map':
            from .segment_dialog import VolumeSegmentationDialog
            d = VolumeSegmentationDialog.get_singleton(session)
        elif tool_name == 'Fit to Segments':
            from .fit_dialog import FitSegmentsDialog
            d = FitSegmentsDialog.get_singleton(session)
        return d

    @staticmethod
    def get_class(class_name):
        # 'get_class' is called by session code to get class saved in a session
        from .regions import Segmentation, Region
        from .segment_dialog import VolumeSegmentationDialog
        from .fit_dialog import FitSegmentsDialog, Fit
        ct = {
            'Segmentation': Segmentation,
            'Region': Region,
            'VolumeSegmentationDialog': VolumeSegmentationDialog,
            'FitSegmentsDialog': FitSegmentsDialog,
            'Fit': Fit,
        }
        return ct.get(class_name)

bundle_api = _SeggerAPI()

# ------------------------------------------------------------------------------
#
dev_menus = False       # Include under-development menus.
timing = False          # Report execution times for optimizing code.
seggerVersion = '2.3'
debug = False		# Whether to output debugging messages

from .regions import Segmentation, Region, SelectedRegions
