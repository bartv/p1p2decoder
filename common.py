from typing import Callable, Sequence, Generic, TypeVar, Type, Tuple
from dataclasses import dataclass

T = TypeVar("T")

NoneType = Type[None]


@dataclass
class Field(Generic[T]):
    """

    :attr position: The byte position in the payload where this field starts
    :attr n_bytes: The number of bytes that are "consumed" by this field
    :attr bitmask: The bitmask to use to get this field when it is a flag
    """

    name: str
    direction: int
    address: int
    packet_type: int

    position: int
    n_bytes: int
    data_type: Callable[[Sequence[int]], T]
    bitmask: int | None = None
    result_type: Type[T] = float

    ignore: Sequence[Sequence[int]] | None = None

    def get_value(self, payload: Sequence[int]) -> T | None:
        if self.ignore is not None:
            for ignore in self.ignore:
                data = payload[self.position : self.position + self.n_bytes]
                if data == ignore:
                    return None

        return self.data_type(payload, self)

def flag(payload: Sequence[int], record: Field) -> bool:
    return bool(payload[record.position] & record.bitmask)

def f8_8(payload: Sequence[int], record: Field) -> float:
    """Fixed point value with the first byte a signed int representing the decimal part and the
    second byte the fractional part
    """
    return payload[record.position] + payload[record.position + 1] / 256


def f8_8r(payload: Sequence[int], record: Field) -> float:
    """Fixed point value with the second byte a signed int representing the decimal part and the
    first byte the fractional part
    """
    return round(payload[record.position + 1] + payload[record.position] / 256, 3)


def f8s8(payload: Sequence[int], record: Field) -> float:
    return round(
        float(payload[record.position]) + float(payload[record.position + 1]) / 10, 3
    )


def u32(payload: Sequence[int], record: Field) -> float:
    if record.n_bytes != 4:
        raise Exception("u32 should always be 4 bytes")

    return (
        payload[record.position] << 3 +
        payload[record.position + 1] << 2 +
        payload[record.position + 2] << 1 +
        payload[record.position + 3]
    )

def u16(payload: Sequence[int], record: Field) -> float:
    if record.n_bytes != 2:
        raise Exception("u16 should always be 2 bytes")

    return (
        payload[record.position + 0] << 1 +
        payload[record.position + 1]
    )

def u8(payload: Sequence[int], record: Field) -> float:
    if record.n_bytes != 1:
        raise Exception("u8 should always be 1 byte")

    return payload[record.position]


def ignore(payload: Sequence[int], record: Field) -> NoneType:
    return None


def hexprint(payload: Sequence[int], record: Field) -> NoneType:
    print(
        f"{record.name}:",
        "".join(
            [
                f"{i:02X}"
                for i in payload[record.position : record.position + record.n_bytes]
            ]
        ),
    )
    return None


def bitprint(payload: Sequence[int], record: Field) -> NoneType:
    print(
        f"{record.name}:",
        "".join(
            [
                f"{i:08b}"
                for i in payload[record.position : record.position + record.n_bytes]
            ]
        ),
    )
    return None
