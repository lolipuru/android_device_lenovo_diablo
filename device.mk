
#
# Copyright (C) 2026 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8475-common
$(call inherit-product, device/lenovo/sm8475-common/common.mk)

# Get non-open-source specific aspects
$(call inherit-product, vendor/lenovo/diablo/diablo-vendor.mk)

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
