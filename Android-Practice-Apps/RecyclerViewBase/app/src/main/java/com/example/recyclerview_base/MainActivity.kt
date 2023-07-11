package com.example.recyclerview_base

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.recyclerview_base.adapter.ItemAdapter
import com.example.recyclerview_base.data.DataSource
import com.example.recyclerview_base.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.recyclerView.layoutManager = LinearLayoutManager(this,
            RecyclerView.VERTICAL,
            false) //Sets to linearLayout through code. Can also be done in main.xml

        // Initialize data.
        val myDataset = DataSource().loadAffirmations()
        binding.recyclerView.adapter = ItemAdapter(this, myDataset)
        // Use this setting to improve performance if you know that changes
        // in content do not change the layout size of the RecyclerView
        binding.recyclerView.setHasFixedSize(true)

    }
}