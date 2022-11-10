def based_on_city(city):
    hotel_data=pd.read_csv('/media/deepu/HardDisk/iitj/Hotel_Recommendation_system/datasets/hotel_data.csv')
    hotel_data['city']=hotel_data['city'].str.lower()
    matched_city=hotel_data[hotel_data['city']==city.lower()]
    matched_city=matched_city.sort_values(by='starrating',ascending=False)
    if matched_city.empty==False:
        data=matched_city.iloc[:,[5,3,2,6,7,8,4,9]]
        count=data.shape[0]
        return data.to_html(index=False),count
    else:
        return "",0
        print("No Hotel Found!")