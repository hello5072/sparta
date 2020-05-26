function is_adult(age, gender) {
    if (age > 60 || age < 10) {
        alert ('탐승하실 수 없습니다')
    }
    else if (age > 20 && gender == '여') {
        alert ('성인 여성')
    }
}

is_adult(10, '여')
