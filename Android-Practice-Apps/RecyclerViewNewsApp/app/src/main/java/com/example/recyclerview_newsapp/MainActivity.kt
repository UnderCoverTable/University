package com.example.recyclerview_newsapp

import ItemClicked
import RecyclerAdapter
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.recyclerview_newsapp.databinding.ActivityMainBinding
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), ItemClicked {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)


        recyclerView.layoutManager = LinearLayoutManager(this) //Uses the same layout as main
        val items = fetchData() // Dummy Data
        val adapter = RecyclerAdapter(items,this) // Uses the adapter functionality
        recyclerView.adapter = adapter

    }

    private fun fetchData():ArrayList<String>{
        val list = ArrayList<String>()
        for(i in 0 until 100){
            list.add("Item -> $i")
        }
        return list
    }

    override fun onItemClicked(item: String) {
        Toast.makeText(this, "CLICKED NUM $item",Toast.LENGTH_SHORT).show()
    }

}

