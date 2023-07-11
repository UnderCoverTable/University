package com.example.recyclerview_base.modal

import androidx.annotation.DrawableRes
import androidx.annotation.StringRes

data class SampleRawData(
    @StringRes val stringResourceId: Int,
    @DrawableRes val imageResourceId: Int)  {
}