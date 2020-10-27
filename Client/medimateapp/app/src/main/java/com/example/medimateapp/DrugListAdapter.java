package com.example.medimateapp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;
import java.util.ArrayList;

public class DrugListAdapter extends BaseAdapter
{
    private TextView contentTextView;
    private TextView titleTextView;

    private ArrayList<DrugItem> drugItemList = new ArrayList<DrugItem>();

    public DrugListAdapter()
    {

    }

    @Override
    public int getCount()
    {
        return drugItemList.size();
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent)
    {
        final int pos = position;
        final Context context = parent.getContext();

        if (convertView == null)
        {
            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.adapter_drug, parent, false);
        }

        titleTextView = (TextView) convertView.findViewById(R.id.title);
        contentTextView = (TextView) convertView.findViewById(R.id.content);

        DrugItem drugItem = drugItemList.get(position);

        titleTextView.setText(drugItem.getTitle());
        contentTextView.setText(drugItem.getContent());

        return convertView;
    }

    @Override
    public long getItemId(int position)
    {
        return position;
    }

    @Override
    public Object getItem(int position)
    {
        return drugItemList.get(position);
    }

    public void addItem(String title, String content)
    {
        DrugItem item = new DrugItem();

        item.setTitle(title);
        item.setContent(content);

        drugItemList.add(item);
    }
}
