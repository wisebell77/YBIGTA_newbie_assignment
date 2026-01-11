
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
# conda가 없는 경우 miniconda 설치
if ! command -v conda &> /dev/null
then
    echo "[INFO] Conda 미설치 확인. Miniconda 설치 진행합니다."
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
    source ~/miniconda3/bin/activate
    conda init bash
    echo "[INFO] Miniconda 설치 완료되었습니다."
fi

# Conda 환경 생성 및 활성화
## TODO
# conda activate 사용 위해 shell 설정 로드
source ~/miniconda3/etc/profile.d/conda.sh 2>/dev/null || cource ~/.bashrc

# 약관 동의 오류 방지 코드
echo "[INFO] Conda 약관 동의 확인"
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main > /dev/null 2>&1 || true
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r > /dev/null 2>&1 || true

# myenv 가상환경 없으면 생성(python 버전은 3.11로)
if ! conda info --envs | grep -q "myenv"; then
    echo "[INFO] myenv 가상환경 생성"
    conda create -n myenv python=3.11 -y
fi

# myenv 활성화
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
echo "[INFO] mypy 설치"
pip install mypy
# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    # 파일명에서 .py 제거
    filename=$(basename "$file" .py)

    input_file="../input/${filename}_input"
    output_file="../output/${filename}_output"

    # 입력 파일이 존재하는지 확인 후 실행
    if [ -f "$input_file" ]; then
        echo "[INFO] $file 실행"
        python "$file" < "$input_file" > "$output_file"
    else
        echo "[INFO] $input_file 이 존재하지 않습니다."
    fi
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
echo "[INFO] mypy 테스트"
mypy *.py > ../mypy_log.txt

# conda.yml 파일 생성
## TODO
echo "[INFO] conda 환경 정보 저장"
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate
echo "[INFO] 가상환경 비활성화"