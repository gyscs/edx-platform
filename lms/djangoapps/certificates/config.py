"""
This module contains various configuration settings via
waffle switches for the Certificates app.
"""

from edx_toggles.toggles import SettingToggle, WaffleSwitch

# Namespace
WAFFLE_NAMESPACE = 'certificates'

# .. toggle_name: certificates.auto_certificate_generation
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: This toggle will enable certificates to be automatically generated
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2017-09-14
AUTO_CERTIFICATE_GENERATION = WaffleSwitch(f"{WAFFLE_NAMESPACE}.auto_certificate_generation", __name__)


# .. toggle_name: SEND_CERTIFICATE_CREATED_SIGNAL
# .. toggle_implementation: SettingToggle
# .. toggle_default: False
# .. toggle_description: When True, we will publish `CERTIFICATE_CREATED` signals to the event bus when a
#   GeneratedCertificate instance with a "passing status" is created/updated. This signal will be consumed by the
#   Credentials IDA in order to keep its records up to date. This is a temporary toggle while we are preparing the
#   Credentials IDA to use the event bus. It should eventually be removed and this functionality should always be
#   enabled.
# .. toggle_use_cases: temporary
# .. toggle_creation_date: 2023-04-11
# .. toggle_target_removal_date: 2023-07-31
# .. toggle_tickets: TODO
SEND_CERTIFICATE_CREATED_SIGNAL = SettingToggle('SEND_CERTIFICATE_CREATED_SIGNAL', default=False, module_name=__name__)
