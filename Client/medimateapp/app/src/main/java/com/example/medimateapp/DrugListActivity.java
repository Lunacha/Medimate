package com.example.medimateapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;

public class DrugListActivity extends AppCompatActivity
{
    private ListView drugList;
    private DrugListAdapter drugAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_druglist);

        drugAdapter = new DrugListAdapter();

        drugList = (ListView) findViewById(R.id.listview);
        drugList.setAdapter(drugAdapter);

        drugAdapter.addItem("hi","test");


        drugAdapter.notifyDataSetChanged();
    }
}