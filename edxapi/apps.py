from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    ProjectType, SettingsType, PluginURLs, PluginSettings, PluginContexts
)

class EdxapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edxapi'

    plugin_app = {

        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {

            # Configure the Plugin URLs for each project type, as needed.
            ProjectType.LMS: {

                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'edxapi',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'edxapi',

                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: r'^api/edxapi/',

                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: 'api.urls',
            }
        },
        # Configuration setting for Plugin Settings for this app.
        PluginSettings.CONFIG: {

            # Configure the Plugin Settings for each Project Type, as needed.
            ProjectType.LMS: {

                # Configure each Settings Type, as needed.
                SettingsType.PRODUCTION: {

                    # The python path (relative to this app) to the settings module for the relevant Project Type and Settings Type.
                    # Optional; Defaults to 'settings'.
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            }
        },

        # Configuration setting for Plugin Signals for this app.
        # PluginSignals.CONFIG: {

        #     # Configure the Plugin Signals for each Project Type, as needed.
        #     ProjectType.LMS: {

        #         # The python path (relative to this app) to the Signals module containing this app's Signal receivers.
        #         # Optional; Defaults to 'signals'.
        #         PluginSignals.RELATIVE_PATH: 'signals',

        #         # List of all plugin Signal receivers for this app and project type.
        #         PluginSignals.RECEIVERS: [{

        #             # The name of the app's signal receiver function.
        #             PluginSignals.RECEIVER_FUNC_NAME: 'on_signal_x',

        #             # The full path to the module where the signal is defined.
        #             PluginSignals.SIGNAL_PATH: 'full_path_to_signal_x_module.SignalX',

        #             # The value for dispatch_uid to pass to Signal.connect to prevent duplicate signals.
        #             # Optional; Defaults to full path to the signal's receiver function.
        #             PluginSignals.DISPATCH_UID: 'my_app.my_signals.on_signal_x',

        #             # The full path to a sender (if connecting to a specific sender) to be passed to Signal.connect.
        #             # Optional; Defaults to None.
        #             PluginSignals.SENDER_PATH: 'full_path_to_sender_app.ModelZ',
        #         }],
        #     }
        # },

        # Configuration setting for Plugin Contexts for this app.
        # PluginContexts.CONFIG: {

        #     # Configure the Plugin Signals for each Project Type, as needed.
        #     ProjectType.LMS: {

        #         # Key is the view that the app wishes to add context to and the value
        #         # is the function within the app that will return additional context
        #         # when called with the original context
        #         'course_dashboard': 'my_app.context_api.get_dashboard_context'
        #     }
        # }
    }