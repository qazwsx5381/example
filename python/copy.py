import os
import shutil

def copy_matching_jpgs(main_folder, jpg_source_folder):
    # 폴더가 진짜 있는지 먼저 확인해줄게!
    if not os.path.isdir(main_folder):
        print(f"앗! '{main_folder}' 폴더가 없는 것 같아요! 경로를 다시 확인해주세요. 😵")
        return
    if not os.path.isdir(jpg_source_folder):
        print(f"이런! '{jpg_source_folder}' 폴더도 없는 것 같아요! 경로를 다시 확인해주세요. 🧐")
        return

    print(f"🌟 '{main_folder}'에 있는 파일 친구들을 위한 짝꿍 .jpg를 '{jpg_source_folder}'에서 찾아볼게요! 🌟")

    copied_count = 0
    not_found_count = 0

    # 'main_folder'에 있는 파일들을 하나씩 살펴볼 거야
    for filename in os.listdir(main_folder):
        # 파일의 이름만 가져올 거야 (확장자는 빼고!)
        # 예를 들어 'document.docx' -> 'document'
        base_name, _ = os.path.splitext(filename)
        
        # 이제 이 이름에 .jpg를 붙여서 'jpg_source_folder'에 있는지 찾아보자!
        matching_jpg_filename = f"{base_name}.jpg"
        source_jpg_path = os.path.join(jpg_source_folder, matching_jpg_filename)
        destination_copy_path = os.path.join(main_folder, matching_jpg_filename)

        # 찾았다 요놈! (뿅!)
        if os.path.exists(source_jpg_path):
            if os.path.exists(destination_copy_path):
                print(f"✔️ '{matching_jpg_filename}'는 이미 '{main_folder}'에 있네요! 스킵~ 🤷‍♀️")
            else:
                print(f"🎉 '{matching_jpg_filename}' 짝꿍을 찾았어요! 복사할게요~!")
                try:
                    shutil.copy2(source_jpg_path, destination_copy_path)
                    copied_count += 1
                except Exception as e:
                    print(f"❌ '{matching_jpg_filename}' 복사하다가 삐끗했어요: {e}")
        else:
            # 으앙, 짝꿍이 없네... 😢
            print(f"🔍 '{base_name}'의 짝꿍 .jpg 파일은 '{jpg_source_folder}'에서 찾을 수 없었어요.")
            not_found_count += 1
    
    print("\n--- 모든 작업이 끝났어요! 야호! ---")
    print(f"💖 총 {copied_count}개의 .jpg 파일을 성공적으로 복사했어요!")
    if not_found_count > 0:
        print(f"💔 아쉽지만 {not_found_count}개의 파일에 해당하는 .jpg 짝꿍은 찾지 못했답니다. 흑흑.")
    print("스크립트가 잘 작동했길 바라! 궁금한 점 있으면 언제든 다시 물어봐줘! 😊")

# === 여기에 네 폴더 경로를 입력해주세요! ===
# 첫 번째 폴더: 여기 파일들의 이름과 똑같은 .jpg 파일을 찾아서 복사해올 곳
main_folder_path = "/Users/ryuyechan/Desktop/사진/2025 가을수련회/작업용" 

# 두 번째 폴더: .jpg 파일들이 모여있는 곳
jpg_source_folder_path = "/Users/ryuyechan/Desktop/사진/2025 가을수련회/jpg" 

# 스크립트를 실행해서 마법을 부려볼까?
copy_matching_jpgs(main_folder_path, jpg_source_folder_path)