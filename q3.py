class Parcel:
    def __init__(self, parcel_id, weight):
        self.parcel_id = parcel_id
        self.weight = weight

    def __str__(self):
        return f"Parcel({self.parcel_id}, {self.weight}kg)"


class DroneUnit:
    def __init__(self, drone_id, capacity):
        self.drone_id = drone_id
        self.capacity = capacity
        self.status = "idle"
        self.active_parcel = None
        self.counter = 0

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        valid = {"idle", "delivering", "charging"}
        if new_status in valid:
            self.status = new_status
        else:
            print(f"Invalid status '{new_status}' for drone {self.drone_id}")

    def assign_parcel(self, parcel):
        if self.status == "idle" and parcel.weight <= self.capacity:
            self.active_parcel = parcel
            self.set_status("delivering")
            self.counter = 2
            print(f"Drone {self.drone_id} started delivering {parcel.parcel_id}")
            return True
        else:
            print(f"Drone {self.drone_id} cannot deliver {parcel.parcel_id}")
            return False

    def tick(self):
        if self.status == "delivering":
            self.counter -= 1
            if self.counter <= 0:
                print(f"Drone {self.drone_id} delivered {self.active_parcel.parcel_id}")
                self.active_parcel = None
                self.set_status("charging")
                self.counter = 2
        elif self.status == "charging":
            self.counter -= 1
            if self.counter <= 0:
                print(f"Drone {self.drone_id} is fully charged and idle now")
                self.set_status("idle")


class FleetControl:
    def __init__(self):
        self.fleet = {}
        self.queue = []

    def register_drone(self, drone):
        self.fleet[drone.drone_id] = drone

    def queue_parcel(self, parcel):
        self.queue.append(parcel)

    def assign_tasks(self):
        for drone in self.fleet.values():
            if drone.get_status() == "idle" and self.queue:
                parcel = self.queue.pop(0)
                if not drone.assign_parcel(parcel):
                    self.queue.insert(0, parcel)

    def simulate(self):
        print("\n=== Cycle Start ===")
        for drone in self.fleet.values():
            drone.tick()
        self.assign_tasks()


if __name__ == "__main__":
    control = FleetControl()
    control.register_drone(DroneUnit("D1", 5))
    control.register_drone(DroneUnit("D2", 10))

    control.queue_parcel(Parcel("P1", 3))
    control.queue_parcel(Parcel("P2", 8))
    control.queue_parcel(Parcel("P3", 4))

    for i in range(6):
        print(f"\n--- Cycle {i + 1} ---")
        control.simulate()
