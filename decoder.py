import sys
import re
import time
from common import Field
import ekh
from typing import Sequence

PACKET = re.compile(r"^([^\s]+) [A-Z] [A-Z]\s+([0-9.]+:)?\s+(?P<packet>[A-Z0-9]+)")


def matches(data: Sequence[int], record: Field) -> Field | None:
    if not data:
        return None

    if data[0] != record.direction:
        return None

    if data[1] != record.address:
        return None

    if data[2] != record.packet_type:
        return None

    return record


def mark_value(body: str, field: Field) -> str:
    """Mark out the bytes used by the given field"""
    return (
        body[: field.position * 2]
        + "**" * field.n_bytes
        + body[field.position * 2 + field.n_bytes * 2 :]
    )


class Decoder:
    """Daiking protocol decoder"""

    def __init__(
        self,
        print_packets: bool = False,
        print_values: bool = False,
        print_masked_packets: bool = False,
        only: Sequence[str] | None = None,
    ) -> None:
        self.print_packets = print_packets
        self.print_values = print_values
        self.print_masked_packets = print_masked_packets

        self.only = only

        self._fields: dict[str, object] = {}
        self._packets: dict[str, str] = {}
        self._masked_packets: dict[str, str] = {}

    def print_packet(self, header: str, payload: str, masked: bool = False) -> None:
        if masked:
            if (
                header not in self._masked_packets
                or self._masked_packets[header] != payload
            ):
                if self.print_masked_packets:
                    print(header, payload)

            self._masked_packets[header] = payload
        else:
            if header not in self._packets or self._packets[header] != payload:
                if self.print_packets:
                    print(header, payload)

            self._packets[header] = payload

    def print_value(self, name: str, value: object) -> None:
        if value is None:
            return

        if name not in self._fields or self._fields[name] != value:
            if self.print_values:
                print(name, value)
        self._fields[name] = value

    def next(self, packet: str) -> None:
        data = []
        for i in range(int(len(packet) / 2)):
            data.append(int(packet[2 * i : 2 * i + 2], 16))

        # check for changes
        header = packet[0:6]
        body = packet[6:-2]

        if not body:
            return

        if self.only and header not in self.only:
            return

        # print(packet)
        # print(f"{header}{body}")
        self.print_packet(header, body)

        # decode the fields
        for field in ekh.fields:
            record = matches(data, field)
            if record:
                self.print_value(record.name, record.get_value(data[3:-1]))
                body = mark_value(body, record)

        self.print_packet(header, body, masked=True)


def main() -> None:
    decode = Decoder(
        print_packets=False,
        print_values=True,
        print_masked_packets=False,
        # only=[
        #     "000010",
        #     "000011",
        #     "000012",
        #     "000020",
        #     "00000D", # a lot of changes
        #     "00000E",
        #     "00000F",
        #     "400010",
        #     "400011",
        #     "400012",
        #     "400020",
        #     "40000D",
        #     "40000E",
        #     "40000F",
        # ],
    )
    while True:
        time.sleep(0.01)
        line = sys.stdin.readline()
        match = PACKET.match(line)
        if match:
            decode.next(match.groupdict()["packet"])


if __name__ == "__main__":
    main()
