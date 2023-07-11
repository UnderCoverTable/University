import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.recyclerview_newsapp.R

class RecyclerAdapter(private val items: ArrayList<String>, private val listener:ItemClicked) : RecyclerView.Adapter<ItemViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_format,parent,false)
        val viewHolder = ItemViewHolder(view)
        view.setOnClickListener{
            listener.onItemClicked(items[viewHolder.adapterPosition])
        }
        return viewHolder
    }

    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        val currentItem = items[position]
        holder.titleView.text = currentItem
    }

    override fun getItemCount(): Int {
        return items.size
    }
}


class ItemViewHolder(itemView : View) : RecyclerView.ViewHolder(itemView)  {
    val titleView: TextView = itemView.findViewById(R.id.title)
}

interface ItemClicked{
    fun onItemClicked(item: String)
}