# weather_forecast

openweathermap.api により天気予報を取得する


APIパラメータ：
（参照）[https://openweathermap.org/api/one-call-api](https://openweathermap.org/api/one-call-api)

取得したjsonデータ内容：　【例】 緯度(lat)=35.7197, 経度(lon)=139.9247

```json
{
    "lat": 35.7197,
    "lon": 139.9247,
    "timezone": "Asia/Tokyo",
    "timezone_offset": 32400,
    "current": {
        "dt": 1615705103,
        "sunrise": 1615668783,
        "sunset": 1615711575,
        "temp": 17.28,
        "feels_like": 9.67,
        "pressure": 1006,
        "humidity": 22,
        "dew_point": -4.09,
        "uvi": 0.63,
        "clouds": 20,
        "visibility": 10000,
        "wind_speed": 7.2,
        "wind_deg": 310,
        "wind_gust": 14.4,
        "weather": [
            {
                "id": 801,
                "main": "Clouds",
                "description": "few clouds",
                "icon": "02d"
            }
        ]
    },
    "daily": [
        {
            "dt": 1615687200,
            "sunrise": 1615668783,
            "sunset": 1615711575,
            "temp": {
                "day": 15.47,
                "min": 10.76,
                "max": 17.28,
                "night": 10.76,
                "eve": 15.61,
                "morn": 12.25
            },
            "feels_like": {
                "day": 4.83,
                "night": 3.43,
                "eve": 6.84,
                "morn": 2.93
            },
            "pressure": 1008,
            "humidity": 23,
            "dew_point": -5.31,
            "wind_speed": 11.39,
            "wind_deg": 310,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": 0,
            "pop": 0.19,
            "uvi": 4.74
        },
        {
            "dt": 1615773600,
            "sunrise": 1615755098,
            "sunset": 1615798026,
            "temp": {
                "day": 13.51,
                "min": 8.66,
                "max": 17.39,
                "night": 13.4,
                "eve": 16.74,
                "morn": 8.91
            },
            "feels_like": {
                "day": 8.02,
                "night": 10.4,
                "eve": 11.94,
                "morn": 2.53
            },
            "pressure": 1016,
            "humidity": 29,
            "dew_point": -4.23,
            "wind_speed": 4.24,
            "wind_deg": 339,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": 0,
            "pop": 0,
            "uvi": 4.35
        },
        {
            "dt": 1615860000,
            "sunrise": 1615841412,
            "sunset": 1615884477,
            "temp": {
                "day": 16.28,
                "min": 11.35,
                "max": 20.73,
                "night": 12.98,
                "eve": 20.73,
                "morn": 11.93
            },
            "feels_like": {
                "day": 11.37,
                "night": 6.05,
                "eve": 15.78,
                "morn": 9.15
            },
            "pressure": 1010,
            "humidity": 33,
            "dew_point": 0.01,
            "wind_speed": 4.18,
            "wind_deg": 253,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": 0,
            "pop": 0,
            "uvi": 5.26
        },
        {
            "dt": 1615946400,
            "sunrise": 1615927726,
            "sunset": 1615970927,
            "temp": {
                "day": 15.6,
                "min": 9.63,
                "max": 17.01,
                "night": 14.32,
                "eve": 15.75,
                "morn": 9.74
            },
            "feels_like": {
                "day": 11.79,
                "night": 10.85,
                "eve": 10.96,
                "morn": 3.23
            },
            "pressure": 1016,
            "humidity": 21,
            "dew_point": -6.55,
            "wind_speed": 1.48,
            "wind_deg": 310,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "clouds": 16,
            "pop": 0,
            "uvi": 5.36
        },
        {
            "dt": 1616032800,
            "sunrise": 1616014039,
            "sunset": 1616057377,
            "temp": {
                "day": 16.05,
                "min": 11.22,
                "max": 16.85,
                "night": 15.44,
                "eve": 16.75,
                "morn": 11.22
            },
            "feels_like": {
                "day": 13.27,
                "night": 12.77,
                "eve": 13.71,
                "morn": 5.99
            },
            "pressure": 1019,
            "humidity": 48,
            "dew_point": 5.27,
            "wind_speed": 2.37,
            "wind_deg": 52,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": 54,
            "pop": 0.01,
            "uvi": 5.68
        },
        {
            "dt": 1616119200,
            "sunrise": 1616100353,
            "sunset": 1616143827,
            "temp": {
                "day": 14.58,
                "min": 12.13,
                "max": 16.52,
                "night": 12.13,
                "eve": 13.63,
                "morn": 13.61
            },
            "feels_like": {
                "day": 10.02,
                "night": 7.26,
                "eve": 7.6,
                "morn": 9.93
            },
            "pressure": 1018,
            "humidity": 49,
            "dew_point": 3.95,
            "wind_speed": 4.63,
            "wind_deg": 68,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 91,
            "pop": 0.34,
            "rain": 0.34,
            "uvi": 6
        },
        {
            "dt": 1616205600,
            "sunrise": 1616186666,
            "sunset": 1616230276,
            "temp": {
                "day": 12.37,
                "min": 10.63,
                "max": 13.87,
                "night": 11.91,
                "eve": 13.87,
                "morn": 10.63
            },
            "feels_like": {
                "day": 9.99,
                "night": 9.87,
                "eve": 12.53,
                "morn": 7.07
            },
            "pressure": 1018,
            "humidity": 77,
            "dew_point": 8.42,
            "wind_speed": 2.89,
            "wind_deg": 148,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 10.41,
            "uvi": 6
        },
        {
            "dt": 1616292000,
            "sunrise": 1616272979,
            "sunset": 1616316726,
            "temp": {
                "day": 20.49,
                "min": 15.42,
                "max": 20.57,
                "night": 15.42,
                "eve": 18.39,
                "morn": 18.19
            },
            "feels_like": {
                "day": 14.88,
                "night": 9.71,
                "eve": 17.45,
                "morn": 10.29
            },
            "pressure": 999,
            "humidity": 53,
            "dew_point": 10.61,
            "wind_speed": 8.31,
            "wind_deg": 225,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 14.66,
            "uvi": 6
        }
    ]
}
```
