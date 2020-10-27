package com.example.medimateapp;

public class DrugItem
{
    private String drugTitle;
    private String drugContent;

    public void setTitle(String title)
    {
        drugTitle = title;
    }
    public void setContent(String content)
    {
        drugContent = content;
    }

    public String getTitle()
    {
        return this.drugTitle;
    }

    public String getContent()
    {
        return this.drugContent;
    }
}
