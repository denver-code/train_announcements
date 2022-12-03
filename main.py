from time import sleep
from playsound import playsound

routes = {
    "2175": {
        "destination":"Littlehampton",
        "from":"London Victoria",
        "calling_at":[
            "London Victoria",
            "Worthing",
            "West Worthing",
            "Littlehampton"
        ]
    }
}

train = routes["2175"]


def notify_station(train, station_name):
    playsound("sounds/general/we_are_now_approaching.mp3")
    playsound(f"sounds/stations/{station_name}.mp3")
    playsound("sounds/general/please_mind_the_gap.mp3")

    sleep(1)

    _train = train
    _train["calling_at"] = _train["calling_at"][_train["calling_at"].index(station_name):]

    start_up_notify(_train)


def start_up_notify(train):
    playsound("sounds/general/welcome_aboard_on_southern_service_to.mp3")
    playsound(f"sounds/stations/{train['destination']}.mp3")
    sleep(0.5)

    playsound("sounds/general/this_train_called_at.mp3")
    for station in train["calling_at"]:
        playsound(f"sounds/stations/{station}.mp3")
        sleep(0.5)

    playsound("sounds/general/the_next_station_is.mp3")
    playsound(f"sounds/stations/{train['calling_at'][1]}.mp3")
    playsound("sounds/general/see_it_say_it_sorted.mp3")


start_up_notify(train)
sleep(1.5)
notify_station(train, "Worthing")