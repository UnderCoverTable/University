package com.example.diceroller

import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // This part hooks all the buttons, Images and text to the object id's
        val rollButton: Button = findViewById(R.id.button)
        val textNum1: TextView = findViewById(R.id.textView1)
        val textNum2: TextView = findViewById(R.id.textView2)
        val textNum3: TextView = findViewById(R.id.textView3)

        val dice1Image: ImageView = findViewById(R.id.imageView1)
        val dice2Image: ImageView = findViewById((R.id.imageView2))
        val dioImage: ImageView = findViewById((R.id.imageView3))

        // Initializes the images
        dice1Image.setImageResource(R.drawable.dice_1)
        dice2Image.setImageResource(R.drawable.dice_6)
        dioImage.setImageResource((android.R.color.transparent))

        // Creates two separate dice
        val sixSideDie1 = Dice(6)
        val sixSideDie2 = Dice(6)

        // Waits for a click on the roll button
        rollButton.setOnClickListener(){
            // Rolls both dice and get a random number
            val diceImageNum1 = sixSideDie1.roll()
            val diceImageNum2 = sixSideDie2.roll()

            // Appropriate number image of dice is shown
            dice1Image.setImageResource(diceImageNum1.first)
            dice2Image.setImageResource(diceImageNum2.first)

            // Shows the number of the dice rolled on the screen
            textNum1.text = diceImageNum1.second.toString()
            textNum2.text = diceImageNum2.second.toString()

            // If both dice roll the same number a message is displayed
            if (diceImageNum1.second == diceImageNum2.second){
                textNum3.text = "DICE ROLLLLAAA DAA"
                dioImage.setImageResource(R.drawable.konodioda)
            }
            else{
                dioImage.setImageResource((android.R.color.transparent))
                textNum3.text ="Not Lucky hoho"
            }

        }

    }

}

// Dice class that basically rolls the dice
class Dice(private val numSides: Int) {

    // functions returns the appropriate image resource and a random number
    fun roll(): Pair<Int,Int> {
        val rolledNum = (1..numSides).random()
        val diceImageNum = when (rolledNum) {
            1 -> R.drawable.dice_1
            2 -> R.drawable.dice_2
            3 -> R.drawable.dice_3
            4 -> R.drawable.dice_4
            5 -> R.drawable.dice_5
            else -> R.drawable.dice_6
        }
        return Pair(diceImageNum,rolledNum)

    }
}
