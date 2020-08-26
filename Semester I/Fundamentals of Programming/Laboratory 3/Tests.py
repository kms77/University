def test_verification_add():
    category=["housekeeping","food","transport","clothing","internet","others"]
    from Verification import verification_add
    cmd=['add','10','food']
    assert(verification_add(cmd,category)==True)
    cmd=['add','10']
    assert(verification_add(cmd,category)==False)
    cmd=['add','at','food']
    assert(verification_add(cmd,category)==False)
    cmd=['add','40','transport']
    assert(verification_add(cmd,category)==True)
    cmd=['add','10','foodd']
    assert(verification_add(cmd,category)==False)
    cmd=['add','-4','food']
    assert(verification_add(cmd,category)==False)
    cmd=['add','food']
    assert(verification_add(cmd,category)==False)
def test_verification_insert():
    category=["housekeeping","food","transport","clothing","internet","others"]
    from Verification import verification_insert
    cmd=['insert','food']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','10','35','housekeeping']
    assert(verification_insert(cmd,category)==True)
    cmd=['insert','31','35','transport']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','20','k','housekeeping']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','and','75','housekeeping']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','10','-235','others']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','10','335','others']
    assert(verification_insert(cmd,category)==True)
    cmd=['insert','10','35','others','yes']
    assert(verification_insert(cmd,category)==False)
    cmd=['insert','10','35','expense']
    assert(verification_insert(cmd,category)==False)
def test_remove():
    from Verification import verify_remove
    category=["housekeeping","food","transport","clothing","internet","others"]
    cmd=['remove','food']
    assert(verify_remove(cmd,category)==True)
    cmd=['remove','house']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','31']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','20']
    assert(verify_remove(cmd,category)==True)
    cmd=['remove','-20']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','-10','to','30']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','1','to','10']
    assert(verify_remove(cmd,category)==True)
    cmd=['remove','10','and','10']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','11','to','31']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','9','to','6']
    assert(verify_remove(cmd,category)==False)
    cmd=['remove','8','to','10','yes']
    assert(verify_remove(cmd,category)==False)
def test_list():
    from Verification import verification_list
    category=["housekeeping","food","transport","clothing","internet","others"]
    cmd=['list']
    assert(verification_list(cmd,category)==True)
    cmd=['list','food']
    assert(verification_list(cmd,category)==True)
    cmd=['list','2']
    assert(verification_list(cmd,category)==False)
    cmd=['list','food','4']
    assert(verification_list(cmd,category)==False)
    cmd=['list','food','>','4']
    assert(verification_list(cmd,category)==True)
    cmd=['list','transport','=',-3]
    assert(verification_list(cmd,category)==False)
    cmd=['list','others','<=',0]
    assert(verification_list(cmd,category)==False)
    cmd=['list','others','>',30]
    assert(verification_list(cmd,category)==True)
    cmd=['list','housekeeping','=','20']
    assert(verification_list(cmd,category)==True)
def test_sum():
    from Verification import verification_sum
    category=["housekeeping","food","transport","clothing","internet","others"]
    cmd=['sum','food']
    assert(verification_sum(cmd,category)==True)
    cmd=['sum','day']
    assert(verification_sum(cmd,category)==False)
    cmd=['sum','3']
    assert(verification_sum(cmd,category)==False)
    cmd=['sum','internet','5']
    assert(verification_sum(cmd,category)==False)
def test_max():
    from Verification import verification_max
    category=["housekeeping","food","transport","clothing","internet","others"]
    cmd=['max','day']
    assert(verification_max(cmd,category)==True)
    cmd=['max']
    assert(verification_max(cmd,category)==False)
    cmd=['max','3','food']
    assert(verification_max(cmd,category)==False)
def test_sort():
    category=["housekeeping","food","transport","clothing","internet","others"]
    from Verification import verification_sort
    cmd=['sort','day']
    assert(verification_sort(cmd,category)==True)
    cmd=['sort','food']
    assert(verification_sort(cmd,category)==True)
    cmd=['sort','33']
    assert(verification_sort(cmd,category)==False)
    cmd=['sort','day','5']
    assert(verification_sort(cmd,category)==False)
    cmd=['sort','food','43','3']
    assert(verification_sort(cmd,category)==False)
def test_validation_filter():
    from Verification import validation_filter
    category=["housekeeping","food","transport","clothing","internet","others"]
    cmd=['filter','food']
    assert(validation_filter(cmd,category)==True)
    cmd=['filter','day']
    assert(validation_filter(cmd,category)==False)
    cmd=['filter']
    assert(validation_filter(cmd,category)==False)
    cmd=['filter','food',3]
    assert(validation_filter(cmd,category)==False)
    cmd=['filter','food','<','3']
    assert(validation_filter(cmd,category)==True)
    cmd=['filter','transport', '=','120']
    assert(validation_filter(cmd,category)==True)
    cmd=['filter','food','<=','6']
    assert(validation_filter(cmd,category)==False)
    cmd=['filter','food','<=','6','h']
    assert(validation_filter(cmd,category)==False)
    cmd=['filter','food','b','a']
    assert(validation_filter(cmd,category)==False)
    cmd=['filter','7','<=','6']
    assert(validation_filter(cmd,category)==False)
def all_tests():
    #all test are calling
    test_verification_add()
    test_verification_insert()
    test_remove()
    test_list()
    test_validation_filter()
    test_sum()
    test_max()
    test_sort()