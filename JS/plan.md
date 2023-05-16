## drag and drop 

```javascript
// 새로고침할 때마다 원복 
function resetUL() {
  const mylist = document.getElementById("plan");
  const ul1 = document.getElementById("ul1");

  // 기본 ul1으로 li 다시 불러오기 
  const uls = mylist.querySelectorAll("ul:not(#ul1)");
  for (const ul of uls) {
    const lis = ul.querySelectorAll("li");
    for (const li of lis) {
      ul.removeChild(li);
      ul1.appendChild(li);
    }
  }

  // 만들었던 ul 다 삭제 
  const otherULs = mylist.querySelectorAll("ul:not(#ul1)");
  for (const ul of otherULs) {
    mylist.removeChild(ul);
  }
}


function calculateDifference() {
  document.getElementById("plan").style.visibility = "visible";
  resetUL();

  // 시작일, 종료일 선택하면 날짜 계산
  const start = new Date(document.getElementById("id_startday_at").value);
  const end = new Date(document.getElementById("id_endday_at").value);
  const differenceInTime = end.getTime() - start.getTime();
  const differenceInDays = Math.floor(differenceInTime / (1000 * 3600 * 24)) + 1;
  document.getElementById("id_day").value = differenceInDays;

  // 계산한 날짜 만큼 ul 생성 (예: Day 1, Day 2 ... )
  for (let i = 1; i <= differenceInDays; i++) {
    const ul = document.createElement("ul");
    ul.classList.add("ul_list", "dropzone", "bg-body-tertiary", "col");
    ul.id = `ul${i + 1}`;
    const mylist = document.getElementById("plan")

    const div = document.createElement("div");
    div.classList.add("text-center", "text-success")
    div.textContent = `Day ${i}`;
    ul.appendChild(div);
    mylist.appendChild(ul);
  };

  const dropzones = document.querySelectorAll('.dropzone');

  // 드래그 시작, 가장 가까운 li 요소로 data transfer 
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('dragstart', (event) => {
      const targetLi = event.target.closest('li');
      if (targetLi) {
        event.dataTransfer.setData('text/plain', targetLi.id);
      }
    });
  });

  // 드롭 가능한 영역으로 들어왔을 때 dragover 이벤트를 처리하여 드래그 요소가 dropzone 요소 위에 올라갈 수 있도록 허용
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('dragover', (event) => {
      event.preventDefault();
    });
  });

  // 드롭한 항목 처리 : dropzone 요소에 대해 drop 이벤트 리스너를 추가
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('drop', (event) => {
      event.preventDefault();

      // 드롭한 data 가져오기 
      const data = event.dataTransfer.getData('text/plain');
      const li = document.getElementById(data);

      // 원래 있던 ul에서 항목 삭제
      li.parentNode.removeChild(li);

      // dropzone에 항목 추가
      dropzone.appendChild(li);

      // li 태그 안에 있는 input 요소의 값을 해당 ul 태그 안에 있는 p 태그 값으로 변경
      const input = li.querySelector('input[name="destination"]');
      const div = dropzone.querySelector('div');
      if (input && div) {
        input.value = div.textContent + '_' + input.value.match(/_(\d+)$/)[1];
      }
    });
  });

  // 여행 날짜에 여행지가 없는 경우 modal
  document.getElementById("plan_form").addEventListener("submit", function (event) {
    const uls = document.querySelectorAll("#plan ul:not(#ul1)");
    for (const ul of uls) {
      const lis = ul.querySelectorAll("li");
      if (lis.length === 0) {
        event.preventDefault();
        Swal.fire(
          `여행 날짜에 여행지를 등록해주세요! <br>${ul.textContent}`
        );
        break;
      }
    }
  });

}

// 중간에 여행 일자가 바뀌면 그에 맞게 수정 
document.getElementById("id_endday_at").addEventListener("change", calculateDifference);


```