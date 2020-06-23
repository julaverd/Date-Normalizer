import re
import datetime
import pandas as pd

def date_sorter():
    # Your code here
    columns = ['Date','Type', 'Year']
    dates=pd.DataFrame(columns=columns)
    date_variants = ['\d{0,2}./\d{0,2}./(?:\d{4}|\d{2})', '\w{3}-\d{2}-\d{4}', '\w{3,}\s\d{2},?\s\d{4}', '\w{3,}.?\s\d{0,2},\s\d{4}', '\d{2}\s\w{3,}.?\s\d{4}', '\w{3}\s\d{2}\w{2},\s\d{4}', '\w{3,},?\s\d{4}', '\d{0,2}.?/\d{4}', '[12]\d{3}', '\d{0,2}.-\d{0,2}.-(?:\d{4}|\d{2})']
    c = []
    month_choices = []
    month_choices_short = []
    for i in range(1,13):
        month_choices.append((datetime.date(2008, i, 1).strftime('%B')))
        month_choices_short.append((datetime.date(2008, i, 1).strftime('%B'))[:3])
    for line in doc:
        for i,exp in enumerate(date_variants):
            date = re.findall(exp, line)
            if date != []:
                if i == 0:
                    pre_date0 = re.split('/', date[0])
                    if len(pre_date0[2]) == 2:
                        if len(pre_date0[1]) == 1:
                            if len(pre_date0[0]) == 1:
                                dates = dates.append({"Date": '19'+pre_date0[2]+'-0'+pre_date0[0]+'-0'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": '19'+pre_date0[2]+'-'+pre_date0[0]+'-0'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                        else:
                            if len(pre_date0[0]) == 1:
                                dates = dates.append({"Date": '19'+pre_date0[2]+'-0'+pre_date0[0]+'-'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                            elif len(pre_date0[0]) == 2:
                                dates = dates.append({"Date": '19'+pre_date0[2]+'-'+pre_date0[0]+'-'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": '19'+pre_date0[2]+'-'+pre_date0[0][:2]+'-'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                    elif len(pre_date0[2]) == 4:
                        if len(pre_date0[1]) == 1:
                            if len(pre_date0[0]) == 1:
                                dates = dates.append({"Date": pre_date0[2]+'-0'+pre_date0[0]+'-0'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": pre_date0[2]+'-'+pre_date0[0]+'-0'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                        else:
                            if len(pre_date0[0]) == 1:
                                dates = dates.append({"Date": pre_date0[2]+'-0'+pre_date0[0]+'-'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": pre_date0[2]+'-'+pre_date0[0]+'-'+pre_date0[1],"Type": i}, ignore_index=True)
                                break
                elif i == 1:
                    pre_date1 = re.split('-', date[0])
                    matching_short = [[t, ind_t] for ind, t in enumerate(month_choices_short) if t in pre_date1[1]]
                    if matching_short != []:
                        dates = dates.append({"Date": pre_date1[2]+'-'+ str(matching_short[0][1]+1) +'-'+pre_date1[1],"Type": i}, ignore_index=True)
                        break
                elif i == 2:
                    pre_date2 = re.split('\s', date[0].replace(',', ''))
                    matching_full = [[s, ind_s] for ind_s, s in enumerate(month_choices) if s in pre_date2[0]]
                    matching_short = [[t, ind_t] for ind_t, t in enumerate(month_choices_short) if t in pre_date2[0]]
                    if matching_full != []:
                        if(len(str(matching_full[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date2[2]+'-0'+ str(matching_full[0][1]+1) +'-'+pre_date2[1],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date2[2]+'-'+ str(matching_full[0][1]+1) +'-'+pre_date2[1],"Type": i}, ignore_index=True)
                            break
                    elif matching_short != []:
                        if(len(str(matching_short[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date2[2]+'-0'+ str(matching_short[0][1]+1) +'-'+pre_date2[1],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date2[2]+'-'+ str(matching_short[0][1]+1) +'-'+pre_date2[1],"Type": i}, ignore_index=True)
                            break
                    else:
                        dates = dates.append({"Date": pre_date2[2]+'-01-01',"Type": i}, ignore_index=True)
                        break
                elif i == 3:
                    pre_date3 = re.split('\s', date[0].replace('.', '').replace(',', ''))
                    matching_full = [[s, ind_s] for ind_s, s in enumerate(month_choices) if s in pre_date3[0]]
                    matching_short = [[t, ind_t] for ind_t, t in enumerate(month_choices_short) if t in pre_date3[0]]
                    if matching_full != []:
                        if(len(str(matching_full[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date3[2]+'-0'+ str(matching_full[0][1]+1) +'-'+pre_date3[1],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date3[2]+'-'+ str(matching_full[0][1]+1) +'-'+pre_date3[1],"Type": i}, ignore_index=True)
                            break
                    elif matching_short != []:
                        if(len(str(matching_short[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date3[2]+'-0'+ str(matching_short[0][1]+1) +'-'+pre_date3[1],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date3[2]+'-'+ str(matching_short[0][1]+1) +'-'+pre_date3[1],"Type": i}, ignore_index=True)
                            break
                    else:
                        dates = dates.append({"Date": pre_date3[2]+'-01-01',"Type": i}, ignore_index=True)
                        break
                elif i == 4:
                    pre_date4 = re.split('\s', date[0].replace('.', ''))
                    matching_full = [[s, ind_s] for ind_s, s in enumerate(month_choices) if s in pre_date4[1]]
                    matching_short = [[t, ind_t] for ind_t, t in enumerate(month_choices_short) if t in pre_date4[1]]
                    if matching_full != []:
                        if(len(str(matching_full[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date4[2]+'-0'+ str(matching_full[0][1]+1) +'-'+pre_date4[0],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date4[2]+'-'+ str(matching_full[0][1]+1) +'-'+pre_date4[0],"Type": i}, ignore_index=True)
                            break
                    elif matching_short != []:
                        if(len(str(matching_short[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date4[2]+'-0'+ str(matching_short[0][1]+1) +'-'+pre_date4[0],"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date4[2]+'-'+ str(matching_short[0][1]+1) +'-'+pre_date4[0],"Type": i}, ignore_index=True)
                            break
                    else:
                        dates = dates.append({"Date": pre_date4[2]+'-01-01',"Type": i}, ignore_index=True)
                        break
                elif i == 5:
                    print(line)
                elif i == 6:
                    pre_date6 = re.split('\s', date[0].replace(',', ''))
                    matching_full = [[s, ind_s] for ind_s, s in enumerate(month_choices) if s in pre_date6[0]]
                    matching_short = [[t, ind_t] for ind_t, t in enumerate(month_choices_short) if t in pre_date6[0]]
                    if matching_full != []:
                        if(len(str(matching_full[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date6[1]+'-0'+ str(matching_full[0][1]+1) +'-01',"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date6[1]+'-'+ str(matching_full[0][1]+1) +'-01',"Type": i}, ignore_index=True)
                            break
                    elif matching_short != []:
                        if(len(str(matching_short[0][1]+1)) == 1):
                            dates = dates.append({"Date": pre_date6[1]+'-0'+ str(matching_short[0][1]+1) +'-01',"Type": i}, ignore_index=True)
                            break
                        else:
                            dates = dates.append({"Date": pre_date6[1]+'-'+ str(matching_short[0][1]+1) +'-01',"Type": i}, ignore_index=True)
                            break
                    else:
                        dates = dates.append({"Date": pre_date6[1]+'-01-01',"Type": i}, ignore_index=True)
                        break
                elif i == 7:
                    pre_date7 = re.split('/', date[0].replace('.', ''))
                    if(len(str(pre_date7[0])) == 1):
                        dates = dates.append({"Date": pre_date7[1]+'-0'+ pre_date7[0] +'-01',"Type": i}, ignore_index=True)
                        break
                    else:
                        dates = dates.append({"Date": pre_date7[1]+'-'+ pre_date7[0] +'-01',"Type": i}, ignore_index=True)
                        break
                elif i == 8:
                    dates = dates.append({"Date": date[0]+'-01-01',"Type": i}, ignore_index=True)
                elif i == 9:
                    pre_date9 = re.split('-', date[0])
                    if len(pre_date9[2]) == 2:
                        if len(pre_date9[1]) == 1:
                            if len(pre_date9[0]) == 1:
                                dates = dates.append({"Date": '19'+pre_date9[2]+'-0'+pre_date9[0]+'-0'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": '19'+pre_date9[2]+'-'+pre_date9[0]+'-0'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                        else:
                            if len(pre_date9[0]) == 1:
                                dates = dates.append({"Date": '19'+pre_date9[2]+'-0'+pre_date9[0]+'-'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                            elif len(pre_date0[0]) == 2:
                                dates = dates.append({"Date": '19'+pre_date9[2]+'-'+pre_date9[0]+'-'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": '19'+pre_date9[2]+'-'+pre_date9[0][:2]+'-'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                    elif len(pre_date9[2]) == 4:
                        if len(pre_date9[1]) == 1:
                            if len(pre_date9[0]) == 1:
                                dates = dates.append({"Date": pre_date9[2]+'-0'+pre_date9[0]+'-0'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": pre_date9[2]+'-'+pre_date9[0]+'-0'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                        else:
                            if len(pre_date9[0]) == 1:
                                dates = dates.append({"Date": pre_date9[2]+'-0'+pre_date9[0]+'-'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
                            else:
                                dates = dates.append({"Date": pre_date9[2]+'-'+pre_date9[0]+'-'+pre_date9[1],"Type": i}, ignore_index=True)
                                break
    dates['Date'] = pd.to_datetime(dates['Date'], format='%Y-%m-%d', errors='ignore')
    dates = dates.sort_values(by='Date',ascending=True, na_position='first')
    return dates.index
