#
# Copyright (C) 2026 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/lenovo/diablo

# Inherit from sm8475-common
include device/lenovo/sm8475-common/BoardConfigCommon.mk

# Inherit from the proprietary version
include vendor/lenovo/diablo/BoardConfigVendor.mk