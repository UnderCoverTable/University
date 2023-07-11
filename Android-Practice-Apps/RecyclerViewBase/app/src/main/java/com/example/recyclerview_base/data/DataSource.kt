package com.example.recyclerview_base.data

import com.example.recyclerview_base.R
import com.example.recyclerview_base.modal.SampleRawData

class DataSource {
    fun loadAffirmations(): List<SampleRawData> {
        return listOf<SampleRawData>(
            SampleRawData(R.string.sample1, R.drawable.image1),
            SampleRawData(R.string.sample2, R.drawable.image2),
            SampleRawData(R.string.sample3, R.drawable.image3),

        )
    }
}
