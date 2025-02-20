import typing

import crcmod.predefined

modbus_crc = crcmod.predefined.mkCrcFun('modbus')


def is_line_protocol_supported(value: typing.Any) -> bool:
    return (
            type(value) is int
            or type(value) is float
            or type(value) is bool
            or type(value) is str
    )


def parse_value(value: typing.Any) -> str:
    if type(value) is int:
        return "%di" % value

    if type(value) is float:
        return "%g" % value

    if type(value) is bool:
        return value and "t" or "f"

    return '"%s"' % escape_value(value)


def escape_value(value: typing.Any) -> str:
    new_value = value.replace("\\", "\\\\")
    new_value = new_value.replace('"', '\\"')

    return new_value
