from ekh import fields


def render_type(field):
    name =  field.data_type.__name__
    if name == "flag":
        return f"{name}({field.bitmask:x})"
    return name


print("| Address | Direction | Packet type | Position | n bytes | data type | name |")
print("| --------| ----------| ------------| ---------| --------| ----------| -----|")
for field in fields:
    #print(field.address, field.direction, field.packet_type, field.position, field.n_bytes, field.data_type, field.name)

    print(
        f"| {field.address:02X} | {field.direction:02X} | {field.packet_type:02X} | {field.position:02d} | "
        f"{field.n_bytes:d} | {render_type(field)} | {field.name} |"
    )