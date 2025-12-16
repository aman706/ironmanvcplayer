from os import path
import asyncio

from helpers.errors import FFmpegReturnCodeError


async def convert(file_path: str) -> str:
    out = path.basename(file_path)
    out = out.split(".")
    out[-1] = "raw"
    out = ".".join(out)
    out = path.basename(out)
    out = path.join("raw_files", out)

    if path.isfile(out):
        return out
    try:
        proc = await asyncio.create_subprocess_shell(
    f"ffmpeg -loglevel error -y -re -i {file_path} "
    f"-ac 2 -ar 48000 "
    f"-c:a libopus -b:a 256k "
    f"-f opus {out}",
        )

        await proc.communicate()

        if proc.returncode != 0:
            raise FFmpegReturnCodeError("FFmpeg did not return 0")

        return out
    except:
        raise FFmpegReturnCodeError("FFmpeg did not return 0")
