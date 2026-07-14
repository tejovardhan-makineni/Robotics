from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OFFLINE = ROOT / "offline"
LOGS = OFFLINE / "logs"


@dataclass(frozen=True)
class Download:
    name: str
    url: str
    destination: Path


PAPERS = [
    Download("open_x_embodiment", "https://arxiv.org/pdf/2310.08864", OFFLINE / "papers" / "open_x_embodiment_2310.08864.pdf"),
    Download("diffusion_policy", "https://arxiv.org/pdf/2303.04137", OFFLINE / "papers" / "diffusion_policy_2303.04137.pdf"),
    Download("mobile_aloha", "https://arxiv.org/pdf/2401.02117", OFFLINE / "papers" / "mobile_aloha_2401.02117.pdf"),
    Download("octo", "https://arxiv.org/pdf/2405.12213", OFFLINE / "papers" / "octo_2405.12213.pdf"),
    Download("openvla", "https://arxiv.org/pdf/2406.09246", OFFLINE / "papers" / "openvla_2406.09246.pdf"),
    Download("pi0", "https://arxiv.org/pdf/2410.24164", OFFLINE / "papers" / "pi0_2410.24164.pdf"),
    Download("smolvla", "https://arxiv.org/pdf/2506.01844", OFFLINE / "papers" / "smolvla_2506.01844.pdf"),
    Download("lerobot", "https://arxiv.org/pdf/2602.22818", OFFLINE / "papers" / "lerobot_2602.22818.pdf"),
    Download("groot_n1", "https://arxiv.org/pdf/2503.14734", OFFLINE / "papers" / "groot_n1_2503.14734.pdf"),
    Download("berkeley_humanoid", "https://arxiv.org/pdf/2407.21781", OFFLINE / "papers" / "berkeley_humanoid_2407.21781.pdf"),
    Download("berkeley_humanoid_lite", "https://arxiv.org/pdf/2504.17249", OFFLINE / "papers" / "berkeley_humanoid_lite_2504.17249.pdf"),
    Download("toddlerbot", "https://arxiv.org/pdf/2502.00893", OFFLINE / "papers" / "toddlerbot_2502.00893.pdf"),
    Download("vla_thinker", "https://arxiv.org/pdf/2603.14523", OFFLINE / "papers" / "vla_thinker_2603.14523.pdf"),
    Download("abot_m0", "https://arxiv.org/pdf/2602.11236", OFFLINE / "papers" / "abot_m0_2602.11236.pdf"),
    Download("xiaomi_robotics_0", "https://arxiv.org/pdf/2602.12684", OFFLINE / "papers" / "xiaomi_robotics_0_2602.12684.pdf"),
    Download("ruka_v2", "https://arxiv.org/pdf/2603.26660", OFFLINE / "papers" / "ruka_v2_2603.26660.pdf"),
    Download("dexora", "https://arxiv.org/pdf/2605.18722", OFFLINE / "papers" / "dexora_2605.18722.pdf"),
    Download("open_eai_platform", "https://arxiv.org/pdf/2606.03392", OFFLINE / "papers" / "open_eai_platform_2606.03392.pdf"),
    Download("robocasa365", "https://arxiv.org/pdf/2603.04356", OFFLINE / "papers" / "robocasa365_2603.04356.pdf"),
]


REPOS = [
    Download("lerobot", "https://github.com/huggingface/lerobot/archive/refs/heads/main.zip", OFFLINE / "repos" / "huggingface_lerobot_main.zip"),
    Download("openpi", "https://github.com/Physical-Intelligence/openpi/archive/refs/heads/main.zip", OFFLINE / "repos" / "physical_intelligence_openpi_main.zip"),
    Download("vla_evaluation_harness", "https://github.com/allenai/vla-evaluation-harness/archive/refs/heads/main.zip", OFFLINE / "repos" / "allenai_vla_evaluation_harness_main.zip"),
    Download("xiaomi_robotics_0", "https://github.com/XiaomiRobotics/Xiaomi-Robotics-0/archive/refs/heads/main.zip", OFFLINE / "repos" / "xiaomi_robotics_0_main.zip"),
    Download("dexora", "https://github.com/dexoravla/Dexora/archive/refs/heads/main.zip", OFFLINE / "repos" / "dexoravla_dexora_main.zip"),
    Download("robotwin", "https://github.com/robotwin-Platform/robotwin/archive/refs/heads/main.zip", OFFLINE / "repos" / "robotwin_platform_robotwin_main.zip"),
    Download("humanoid_gym", "https://github.com/roboterax/humanoid-gym/archive/refs/heads/main.zip", OFFLINE / "repos" / "roboterax_humanoid_gym_main.zip"),
    Download("openarm", "https://github.com/reazon-research/openarm/archive/refs/heads/main.zip", OFFLINE / "repos" / "reazon_research_openarm_main.zip"),
]


def ensure_dirs() -> None:
    for path in [
        OFFLINE,
        OFFLINE / "papers",
        OFFLINE / "repos",
        OFFLINE / "wheels" / "core",
        LOGS,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def run_pip_download() -> dict:
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "download",
        "-r",
        str(ROOT / "requirements.txt"),
        "-d",
        str(OFFLINE / "wheels" / "core"),
    ]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    (LOGS / "pip_download_core.log").write_text(result.stdout + "\n" + result.stderr)
    return {
        "command": cmd,
        "returncode": result.returncode,
        "ok": result.returncode == 0,
        "log": str((LOGS / "pip_download_core.log").relative_to(ROOT)),
    }


def download_file(item: Download) -> dict:
    if item.destination.exists() and item.destination.stat().st_size > 0:
        return {"name": item.name, "url": item.url, "path": str(item.destination.relative_to(ROOT)), "ok": True, "cached": True}

    tmp = item.destination.with_suffix(item.destination.suffix + ".part")
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--retry",
        "3",
        "--connect-timeout",
        "20",
        "--max-time",
        "300",
        "-A",
        "robotics-offline-bundle/1.0",
        "-o",
        str(tmp),
        item.url,
    ]
    try:
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            if tmp.exists():
                tmp.unlink()
            return {
                "name": item.name,
                "url": item.url,
                "path": str(item.destination.relative_to(ROOT)),
                "ok": False,
                "returncode": result.returncode,
                "error": (result.stderr or result.stdout).strip()[-800:],
            }
        tmp.replace(item.destination)
        return {
            "name": item.name,
            "url": item.url,
            "path": str(item.destination.relative_to(ROOT)),
            "ok": item.destination.exists() and item.destination.stat().st_size > 0,
            "bytes": item.destination.stat().st_size if item.destination.exists() else 0,
        }
    except Exception as exc:
        if tmp.exists():
            tmp.unlink()
        return {"name": item.name, "url": item.url, "path": str(item.destination.relative_to(ROOT)), "ok": False, "error": str(exc)}


def main() -> int:
    ensure_dirs()
    manifest = {
        "core_wheels": run_pip_download(),
        "papers": [download_file(item) for item in PAPERS],
        "repos": [download_file(item) for item in REPOS],
    }
    (LOGS / "manifest.json").write_text(json.dumps(manifest, indent=2))

    ok_papers = sum(1 for item in manifest["papers"] if item["ok"])
    ok_repos = sum(1 for item in manifest["repos"] if item["ok"])
    print(f"core wheels ok: {manifest['core_wheels']['ok']}")
    print(f"papers downloaded: {ok_papers}/{len(PAPERS)}")
    print(f"repo snapshots downloaded: {ok_repos}/{len(REPOS)}")
    print(f"manifest: {(LOGS / 'manifest.json').relative_to(ROOT)}")
    return 0 if manifest["core_wheels"]["ok"] and ok_papers and ok_repos else 1


if __name__ == "__main__":
    raise SystemExit(main())
