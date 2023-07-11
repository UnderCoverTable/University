package com.example.planets

import android.media.MediaPlayer
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.planets.databinding.ActivityMainBinding
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), ItemClicked {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)


        // Calls updateStuffSpinner when an item is selected in the spinner
        binding.spinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(p0: AdapterView<*>?, p1: View?, p2: Int, p3: Long) {
                updateStuffSpinner()
            }

            override fun onNothingSelected(p0: AdapterView<*>?) {
                TODO("Not yet implemented")
            }
        }
        // Calls updateStuffRadio when a radio button is clicked
        binding.radioGroup.setOnCheckedChangeListener { _, _ ->
            updateStuffRadio()
        }

        // Calls updateStuffButton whenever the button is clicked
        binding.button.setOnClickListener {
            updateStuffButton()
        }

        recyclerView.layoutManager = LinearLayoutManager(this) //Uses the same layout as main
        val planetItems : List<String> = listOf("Mercury","Venus","Earth","Mars","Jupiter",
            "Saturn","Uranus","Neptune","Pluto","Kars")
        val adapter = RecyclerAdapter(planetItems,this) // Uses the adapter functionality
        recyclerView.adapter = adapter

    }

    // Function to reset the image, text, radio button and spinner to Earth
    private fun updateStuffButton() {
        binding.imageView.setImageResource(R.drawable.earth)
        binding.textView.text = getString(R.string.planetEarth)
        binding.radioButton3.toggle()
        binding.spinner.setSelection(2)
    }

    // Updates the image, text and radio button whenever a planet is selected from the spinner
    fun updateStuffSpinner() {
        val planetImage = binding.imageView
        val planetRadio1 = binding.radioButton
        val planetRadio2 = binding.radioButton2
        val planetRadio3 = binding.radioButton3
        val planetRadio4 = binding.radioButton4
        val planetRadio7 = binding.radioButton7
        val planetRadio8 = binding.radioButton8
        val planetRadio9 = binding.radioButton9
        val planetRadio10 = binding.radioButton10
        val planetRadio11 = binding.radioButton11
        val mp = MediaPlayer.create(this, R.raw.aztec_dubstep)


        when (binding.spinner.selectedItem.toString()) {
            "Mercury" -> {
                planetImage.setImageResource(R.drawable.mercury)
                binding.textView.text = getString(R.string.planetMercury)
                planetRadio1.toggle()
            }
            "Venus" -> {
                planetImage.setImageResource(R.drawable.venus)
                binding.textView.text = getString(R.string.planetVenus)
                planetRadio2.toggle()
            }
            "Earth" -> {
                planetImage.setImageResource(R.drawable.earth)
                binding.textView.text = getString(R.string.planetEarth)
                planetRadio3.toggle()
            }
            "Mars" -> {
                planetImage.setImageResource(R.drawable.mars)
                binding.textView.text = getString(R.string.planetMars)
                planetRadio4.toggle()
            }
            "Jupiter" -> {
                planetImage.setImageResource(R.drawable.jupiter)
                binding.textView.text = getString(R.string.planetJupiter)
                planetRadio7.toggle()
            }
            "Saturn" -> {
                planetImage.setImageResource(R.drawable.saturn)
                binding.textView.text = getString(R.string.planetSaturn)
                planetRadio8.toggle()
            }
            "Uranus" -> {
                planetImage.setImageResource(R.drawable.uranus)
                binding.textView.text = getString(R.string.planetUranus)
                planetRadio9.toggle()
            }
            "Neptune" -> {
                planetImage.setImageResource(R.drawable.neptune)
                binding.textView.text = getString(R.string.planetNeptune)
                planetRadio10.toggle()
            }
            "Pluto" -> {
                if(mp.isPlaying){
                    mp.stop()
                }
                planetImage.setImageResource(R.drawable.pluto)
                binding.textView.text = getString(R.string.planetPluto)
                planetRadio11.toggle()
            }
            "Kars" -> {
                planetImage.setImageResource(R.drawable.kars1)
                mp.start()
                binding.textView.text = getString(R.string.planetKars)
                Toast.makeText(this,"ゴゴゴゴゴ",Toast.LENGTH_SHORT).show()

            }

        }
    }

    // Updates the Image, text and spinner when a planet is selected from the radio group
    private fun updateStuffRadio() {
        val planetImage = binding.imageView

        val planetRadio1 = binding.radioButton
        val planetRadio2 = binding.radioButton2
        val planetRadio3 = binding.radioButton3
        val planetRadio4 = binding.radioButton4
        val planetRadio7 = binding.radioButton7
        val planetRadio8 = binding.radioButton8
        val planetRadio9 = binding.radioButton9
        val planetRadio10 = binding.radioButton10
        val planetRadio11 = binding.radioButton11

        val spinnerPlanet = binding.spinner


        if (planetRadio1.isChecked) {
            planetImage.setImageResource(R.drawable.mercury)
            spinnerPlanet.setSelection(0)
            binding.textView.text = getString(R.string.planetMercury)

        }
        if (planetRadio2.isChecked) {
            planetImage.setImageResource(R.drawable.venus)
            spinnerPlanet.setSelection(1)
            binding.textView.text = getString(R.string.planetVenus)
        }
        if (planetRadio3.isChecked) {
            planetImage.setImageResource(R.drawable.earth)
            spinnerPlanet.setSelection(2)
            binding.textView.text = getString(R.string.planetEarth)
        }
        if (planetRadio4.isChecked) {
            planetImage.setImageResource(R.drawable.mars)
            spinnerPlanet.setSelection(3)
            binding.textView.text = getString(R.string.planetMars)
        }
        if (planetRadio7.isChecked) {
            planetImage.setImageResource(R.drawable.jupiter)
            spinnerPlanet.setSelection(4)
            binding.textView.text = getString(R.string.planetJupiter)
        }
        if (planetRadio8.isChecked) {
            planetImage.setImageResource(R.drawable.saturn)
            spinnerPlanet.setSelection(5)
            binding.textView.text = getString(R.string.planetSaturn)
        }
        if (planetRadio9.isChecked) {
            planetImage.setImageResource(R.drawable.uranus)
            spinnerPlanet.setSelection(6)
            binding.textView.text = getString(R.string.planetUranus)
        }
        if (planetRadio10.isChecked) {
            planetImage.setImageResource(R.drawable.neptune)
            spinnerPlanet.setSelection(7)
            binding.textView.text = getString(R.string.planetNeptune)
        }
        if (planetRadio11.isChecked) {
            planetImage.setImageResource(R.drawable.pluto)
            spinnerPlanet.setSelection(8)
            binding.textView.text = getString(R.string.planetMars)
        }


    }

    override fun onItemClicked(item: String) {
        val planetImage = binding.imageView
        val spinnerPlanet = binding.spinner

        val planetRadio1 = binding.radioButton
        val planetRadio2 = binding.radioButton2
        val planetRadio3 = binding.radioButton3
        val planetRadio4 = binding.radioButton4
        val planetRadio7 = binding.radioButton7
        val planetRadio8 = binding.radioButton8
        val planetRadio9 = binding.radioButton9
        val planetRadio10 = binding.radioButton10
        val planetRadio11 = binding.radioButton11

        when(item){
            "Mercury" ->{
                planetImage.setImageResource(R.drawable.mercury)
                binding.textView.text = getString(R.string.planetMercury)
                planetRadio1.toggle()
                spinnerPlanet.setSelection(0)

            }
            "Venus" ->{
                planetImage.setImageResource(R.drawable.venus)
                binding.textView.text = getString(R.string.planetVenus)
                planetRadio2.toggle()
                spinnerPlanet.setSelection(1)

            }
            "Earth" ->{
                planetImage.setImageResource(R.drawable.earth)
                binding.textView.text = getString(R.string.planetEarth)
                planetRadio3.toggle()
                spinnerPlanet.setSelection(2)

            }
            "Mars" ->{
                planetImage.setImageResource(R.drawable.mars)
                binding.textView.text = getString(R.string.planetMars)
                planetRadio4.toggle()
                spinnerPlanet.setSelection(3)

            }
            "Jupiter" ->{
                planetImage.setImageResource(R.drawable.jupiter)
                binding.textView.text = getString(R.string.planetJupiter)
                planetRadio7.toggle()
                spinnerPlanet.setSelection(4)

            }
            "Saturn" ->{
                planetImage.setImageResource(R.drawable.saturn)
                binding.textView.text = getString(R.string.planetSaturn)
                planetRadio8.toggle()
                spinnerPlanet.setSelection(5)

            }
            "Uranus" ->{
                planetImage.setImageResource(R.drawable.uranus)
                binding.textView.text = getString(R.string.planetUranus)
                planetRadio9.toggle()
                spinnerPlanet.setSelection(6)

            }
            "Neptune" ->{
                planetImage.setImageResource(R.drawable.neptune)
                binding.textView.text = getString(R.string.planetNeptune)
                planetRadio10.toggle()
                spinnerPlanet.setSelection(7)

            }
            "Pluto" ->{
                planetImage.setImageResource(R.drawable.pluto)
                binding.textView.text = getString(R.string.planetPluto)
                planetRadio11.toggle()
                spinnerPlanet.setSelection(8)
            }
            "Kars" ->{
                planetImage.setImageResource(R.drawable.kars1)
                val mp = MediaPlayer.create(this, R.raw.aztec_dubstep)
                mp.start()
                binding.textView.text = getString(R.string.planetKars)
                spinnerPlanet.setSelection(9)
                Toast.makeText(this,"ゴゴゴゴゴ",Toast.LENGTH_SHORT).show()


            }



        }
    }
}
