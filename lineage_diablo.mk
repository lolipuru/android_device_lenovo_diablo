#
# Copyright (C) 2026 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from diablo device.
$(call inherit-product, device/lenovo/diablo/device.mk)

## Device identifier
PRODUCT_DEVICE := diablo
PRODUCT_NAME := lineage_diablo
PRODUCT_BRAND := lenovo
PRODUCT_MODEL := Legion Y90
PRODUCT_MANUFACTURER := lenovo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc=$(call normalize-path-list, "Lenovo diablo diablo 12 SKQ1.211113.001 14.0.120_221208:user release-keys")

BUILD_FINGERPRINT := Lenovo/diablo/diablo:12/SKQ1.211113.001/14.0.120_221208:user/release-keys

# GMS
PRODUCT_GMS_CLIENTID_BASE := android-lenovo