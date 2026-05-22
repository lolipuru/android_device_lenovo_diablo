#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/lenovo/diablo',
    'device/lenovo/sm8475-common',
    'hardware/qcom-caf/sm8450',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/lenovo/sm8475-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/bin/hw/android.hardware.gnss-aidl-service-qti',
        'vendor/lib64/hw/android.hardware.gnss-aidl-impl-qti.so',
        'vendor/lib64/libgarden.so',
        'vendor/lib64/libgarden_haltests_e2e.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.gnss-V1-ndk_platform.so',
            'android.hardware.gnss-V1-ndk.so',
        ),
    'vendor/bin/hw/vendor.qti.hardware.display.composer-service': blob_fixup()
        .replace_needed('android.hardware.common-V2-ndk_platform.so', 'android.hardware.common-V2-ndk.so')
        .replace_needed('vendor.qti.hardware.display.config-V4-ndk_platform.so', 'vendor.qti.hardware.display.config-V5-ndk.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed(
            'vendor.qti.hardware.display.config-V2-ndk_platform.so',
            'vendor.qti.hardware.display.config-V2-ndk.so',
        ),
    (
        'vendor/lib64/libpandora.render.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
}

module = ExtractUtilsModule(
    'diablo',
    'lenovo',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()