package com.example.recyclerview_base.adapter

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.recyclerview_base.R
import com.example.recyclerview_base.modal.SampleRawData

class ItemAdapter(
    private val context: Context,
    private val dataset: List<SampleRawData>
) : RecyclerView.Adapter<ItemAdapter.ItemViewHolder>() {

    class ItemViewHolder(private val view: View) : RecyclerView.ViewHolder(view) {
        val textView: TextView = view.findViewById(R.id.itemTextView)
        val imageView: ImageView = view.findViewById(R.id.itemImageView)
    }

    //create a new view holder (if it doesn't exists)
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val adapterLayout = LayoutInflater.from(parent.context)
            .inflate(R.layout.list_item, parent, false)

        return ItemViewHolder(adapterLayout)    }

    //here we modify the view holder items to show on screen
    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        val item = dataset[position]
        holder.textView.text =  context.resources.getString(item.stringResourceId)
        holder.imageView.setImageResource(item.imageResourceId)}

    //returns total number of elements
    override fun getItemCount(): Int {
        return dataset.size
    }

}

