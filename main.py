"""Write the pigeon-apology pitch to /output/entry.txt.

The pitch: we train pigeons to deliver handwritten apology notes to
blocked exes. It sounds ridiculous at first glance — a bird courier
for a text message era — but it is a real business: the blocked ex
cannot swipe a bird away, cannot leave it on read, and cannot block
a pigeon. A handwritten sorry that physically arrives is the one
apology that forces a read, so people who have run out of digital
channels will pay for the one channel that cannot be muted.

One sentence, 158 chars, written exactly as-is, no trailing newline.
"""

import os

LINE = (
    "We train pigeons to deliver handwritten apology notes to blocked exes, "
    "because a sorry carried by a bird is the only apology they cannot "
    "swipe away unread."
)


def write_entry(path: str, line: str) -> None:
    """Write the pitch bytes to path, readable by the grader (0644)."""
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), LINE)


if __name__ == "__main__":
    main()
