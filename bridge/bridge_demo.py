from abc import ABC, abstractmethod


# Implementation interface
class Device(ABC):
    """
    The Implementation interface declares methods common to all concrete implementations.
    The Abstraction's methods call implementation methods through this interface.
    """

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        pass


# Concrete Implementations
class TV(Device):
    """Concrete Implementation for TV"""

    def __init__(self):
        self._enabled = False
        self._volume = 30
        self._channel = 1

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True
        print("TV: powered on")

    def disable(self) -> None:
        self._enabled = False
        print("TV: powered off")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        if percent < 0:
            self._volume = 0
        elif percent > 100:
            self._volume = 100
        else:
            self._volume = percent
        print(f"TV: volume set to {self._volume}%")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = channel
        print(f"TV: channel set to {self._channel}")


class Radio(Device):
    """Concrete Implementation for Radio"""

    def __init__(self):
        self._enabled = False
        self._volume = 20
        self._channel = 88.5  # FM frequency

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True
        print("Radio: turned on")

    def disable(self) -> None:
        self._enabled = False
        print("Radio: turned off")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        if percent < 0:
            self._volume = 0
        elif percent > 100:
            self._volume = 100
        else:
            self._volume = percent
        print(f"Radio: volume set to {self._volume}%")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = channel
        print(f"Radio: station set to {self._channel} FM")


# Abstraction
class RemoteControl:
    """
    The Abstraction defines the interface for the control part of the two class hierarchies.
    It maintains a reference to an object of the Implementation hierarchy and delegates
    all of the real work to this object.
    """

    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self) -> None:
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self) -> None:
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self) -> None:
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self) -> None:
        self._device.set_channel(self._device.get_channel() + 1)


# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def mute(self) -> None:
        self._device.set_volume(0)

    def jump_to_channel(self, channel: int) -> None:
        self._device.set_channel(channel)


# Client code
def client_code():
    # Using a basic remote with TV
    tv = TV()
    remote = RemoteControl(tv)

    print("Testing basic remote with TV:")
    remote.toggle_power()
    remote.channel_up()
    remote.volume_up()
    remote.toggle_power()

    print("\n------------------------------\n")

    # Using an advanced remote with Radio
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)

    print("Testing advanced remote with Radio:")
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.jump_to_channel(103.5)
    advanced_remote.mute()
    advanced_remote.toggle_power()


if __name__ == "__main__":
    client_code()