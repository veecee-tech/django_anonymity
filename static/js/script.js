var _a;
console.log('start of script');
console.log('hi');


const menu = document.querySelector('[data-menu]');
const closeBtn = document.querySelector('[data-closeBtn]');
const nav = document.querySelector('[data-nav]');
const report_case_btn = document.querySelectorAll('[data-report_case_btn]');
const reportFasle = document.querySelector('[data-report="false"]');
const reportTrue = document.querySelector('[data-report="true"]');
const prevStep1 = document.querySelector('[data-prevStep1]');
const nextStep1 = document.querySelector('[data-nextStep1]');
const prevStep2 = document.querySelector('[data-prevStep2]');
const nextStep2 = document.querySelector('[data-nextStep2]');
const prevStep3 = document.querySelector('[data-prevStep3]');
const submitReport = document.querySelector('[data-submitReport]');
const section1 = document.querySelector('[data-section="1"]');
const section2 = document.querySelector('[data-section="2"]');
const section3 = document.querySelector('[data-section="3"]');
const selectFile = document.querySelector('[data-selectFile]');
const selectedFile = document.querySelector('[data-selectedFile]');
const submitReportOverlay = document.querySelector('[data-overlay]');
const closeReportOverlay = document.querySelectorAll('[data-closeOverlay]');
const questionHeaders = document.querySelectorAll('[data-questionHeader]');
const questionBodys = document.querySelectorAll('[data-questionBody]');
const items = document.querySelectorAll('[data-item]');
const unselectedDiv = document.querySelector('[data-selected="false"]');
const selectedDiv = document.querySelector('[data-selected="true"]');
const goBackUnselectedBtn = document.querySelector('[data-goBackUnselected]');
const hideIdentityBtn = document.querySelector('[data-identity="true"]');
const dontHideIdentityBtn = document.querySelector('[data-identity="false"]');
const chooseIdentityDiv = document.querySelector('[data-chooseIdentity]');
const successDiv = document.querySelector('[data-success]');
const loginBtn = document.querySelector('[data-login]');
const dashboardUL = document.querySelector('[data-dashboardUL]');
const dashboardLink = document.querySelector('[data-dashboardLink]');
const profileLink = document.querySelector('[data-profileLink]');
const dashboardItems = document.querySelector("[data-dashboardItems]");
const dashbaordSection = document.querySelector('[data-dashbaordSection]');
const profileSection = document.querySelector('[data-profileSection]');
const userDashboardMenu = document.querySelector('[data-userDashboardMenu]');
const userDashboardClose = document.querySelector('[data-userDashboardClose]');
const userDashboardAside = document.querySelector('[data-userDashboardAside]');
const userDashboardOverlay = document.querySelector('.overlay');
const userDetails = document.querySelector('[data-userDetails]');
const closeUserDetails = document.querySelector('[data-closeUserDetails]');
// admin dashboard starts
closeUserDetails === null || closeUserDetails === void 0 ? void 0 : closeUserDetails.addEventListener('click', () => {
    userDetails.classList.toggle('hide');
});
// admin dashbaord ends
// user dashbaord starts
userDashboardMenu === null || userDashboardMenu === void 0 ? void 0 : userDashboardMenu.addEventListener('click', () => {
    userDashboardAside.classList.toggle('animateFromLeft');
    userDashboardClose.classList.toggle('hide');
    userDashboardMenu.classList.toggle('hide');
    userDashboardOverlay.classList.toggle('openOverlay');
});
userDashboardClose === null || userDashboardClose === void 0 ? void 0 : userDashboardClose.addEventListener('click', () => {
    userDashboardAside.classList.toggle('animateFromLeft');
    userDashboardClose.classList.toggle('hide');
    userDashboardMenu.classList.toggle('hide');
    userDashboardOverlay.classList.toggle('openOverlay');
});
if (dashboardUL) {
    (_a = Array.from(dashboardUL === null || dashboardUL === void 0 ? void 0 : dashboardUL.children)) === null || _a === void 0 ? void 0 : _a.forEach(element1 => {
        element1.addEventListener('click', () => {
            [...dashboardUL === null || dashboardUL === void 0 ? void 0 : dashboardUL.children].forEach(element2 => {
                if (element1 == element2)
                    return;
                element1.classList.add('activeTab');
                element2.classList.remove('activeTab');
                Array.from(dashboardItems.children).forEach(item => {
                    const ulClass = element1.getAttribute('id');
                    if (ulClass == null || ulClass == undefined || ulClass == "")
                        return;
                    if (item.classList.contains(ulClass)) {
                        item.classList.remove('hide');
                    }
                    else {
                        item.classList.add('hide');
                    }
                });
            });
            userDashboardClose.click();
        });
    });
}
//user dashboard ends
let pickedFile;
//start login
loginBtn === null || loginBtn === void 0 ? void 0 : loginBtn.addEventListener('click', () => {
    window.location.href = '/src/pages/user_dashboard';
});
//end login
// start faq  
goBackUnselectedBtn === null || goBackUnselectedBtn === void 0 ? void 0 : goBackUnselectedBtn.addEventListener('click', () => {
    selectedDiv.classList.add('hide');
    unselectedDiv.classList.remove('hide');
});
let observer;
let options = {
    root: document.querySelector('.secondContainer'),
    rootMargin: '50px',
    threshold: .5,
};
observer = new IntersectionObserver(callback, options);
items.forEach(item => {
    observer.observe(item);
});
function callback(items) {
    items.forEach(item => {
        const insIntersecting = item.isIntersecting;
        const targetElem = item.target;
        insIntersecting ? targetElem.classList.add('scale') : targetElem.classList.remove('scale');
    });
}
items === null || items === void 0 ? void 0 : items.forEach(item => item.addEventListener('click', () => {
    const imgSrc = item.children[0].getAttribute('src');
    const blogBody = item.querySelector('[data-blog-body-unselected]').textContent;
    const blogTitle = item.querySelector('[data-blog-title-unselected]').textContent;
    const blogCreatedAt = item.querySelector('[data-blog-created-at-unselected]').textContent;
    
    console.log(blogBody);
    unselectedDiv.classList.add('hide');
    selectedDiv.classList.remove('hide');
    selectedDiv.querySelector('[data-dynamicImg]').setAttribute('src', imgSrc);
    selectedDiv.querySelector('[data-blog-body-selected]').textContent= blogBody;
    selectedDiv.querySelector('[data-blog-title-selected]').textContent=blogTitle;
    selectedDiv.querySelector('[data-blog-created-at-selected]').textContent=blogCreatedAt;
}));

// items.forEach(element => {
//     let textContent = element.querySelector('[data-blog-body-unselected]').textContent;
//     element.querySelector('[data-blog-body-unselected]').textContent = textContent.slice(0,50)+'...';

// });

questionHeaders === null || questionHeaders === void 0 ? void 0 : questionHeaders.forEach((header, index) => {
    header.addEventListener('click', () => {
        questionBodys.forEach((elem, idx) => {
            if (index == idx)
                return;
            elem.classList.remove('open');
            elem.setAttribute('style', `height:0px`);
            questionHeaders.forEach((head, idx) => {
                if (index == idx)
                    return;
                const plusIcon = head.querySelector('[data-plus]');
                const timesIcon = head.querySelector('[data-times]');
                plusIcon.classList.remove('hide');
                timesIcon.classList.add('hide');
            });
        });
        const qstnBody = header.parentElement.children[1];
        qstnBody.classList.toggle('open');
        if (qstnBody.classList.contains('open'))
            qstnBody.setAttribute('style', `height:${qstnBody.scrollHeight}px`);
        else
            qstnBody.setAttribute('style', `height:0px`);
        const plusIcon = header.querySelector('[data-plus]');
        const timesIcon = header.querySelector('[data-times]');
        plusIcon.classList.toggle('hide');
        timesIcon.classList.toggle('hide');
    });
});
// end faq  
closeReportOverlay === null || closeReportOverlay === void 0 ? void 0 : closeReportOverlay.forEach((elem, index) => elem.addEventListener('click', () => {
    submitReportOverlay.classList.toggle('hide');
    if (index == 1) {
        chooseIdentityDiv.classList.remove('hide');
        successDiv.classList.add('hide');
        reportFasle.classList.remove('hide');
        reportTrue.classList.add('hide');
        document.body.scrollIntoView();
    }
}));
hideIdentityBtn === null || hideIdentityBtn === void 0 ? void 0 : hideIdentityBtn.addEventListener('click', () => {
    chooseIdentityDiv.classList.add('hide');
    successDiv.classList.remove('hide');
});
dontHideIdentityBtn === null || dontHideIdentityBtn === void 0 ? void 0 : dontHideIdentityBtn.addEventListener('click', () => {
    chooseIdentityDiv.classList.add('hide');
    successDiv.classList.remove('hide');
});
submitReport === null || submitReport === void 0 ? void 0 : submitReport.addEventListener('click', () => {
    submitReportOverlay.classList.toggle('hide');
});
selectFile === null || selectFile === void 0 ? void 0 : selectFile.addEventListener('change', (e) => {
    const target = e.target;
    pickedFile = target.files[0];
    selectedFile.innerText = target.files[0].name;
});
if (report_case_btn) {
    console.log(report_case_btn);
}
else {
    console.log('else');
}
report_case_btn === null || report_case_btn === void 0 ? void 0 : report_case_btn.forEach(btn => {
    btn === null || btn === void 0 ? void 0 : btn.addEventListener('click', () => {
        reportFasle.classList.add('hide');
        reportTrue.classList.remove('hide');
        section1.parentElement.scrollIntoView({ behavior: "smooth" });
    });
});
prevStep1 === null || prevStep1 === void 0 ? void 0 : prevStep1.addEventListener('click', () => {
    reportFasle.classList.remove('hide');
    reportTrue.classList.add('hide');
});
nextStep1 === null || nextStep1 === void 0 ? void 0 : nextStep1.addEventListener('click', () => {
    section1.classList.add('hide');
    section2.classList.remove('hide');
    section2.parentElement.scrollIntoView({ behavior: 'smooth' });
});
prevStep2 === null || prevStep2 === void 0 ? void 0 : prevStep2.addEventListener('click', () => {
    section1.classList.remove('hide');
    section2.classList.add('hide');
    section1.parentElement.scrollIntoView({ behavior: "smooth" });
});
nextStep2 === null || nextStep2 === void 0 ? void 0 : nextStep2.addEventListener('click', () => {
    section2.classList.add('hide');
    section3.classList.remove('hide');
    section3.parentElement.scrollIntoView({ behavior: 'smooth' });
});
prevStep3 === null || prevStep3 === void 0 ? void 0 : prevStep3.addEventListener('click', () => {
    section2.classList.remove('hide');
    section3.classList.add('hide');
    section2.parentElement.scrollIntoView({ behavior: 'smooth' });
});
menu === null || menu === void 0 ? void 0 : menu.addEventListener('click', () => {
    nav.classList.add('open');
});
closeBtn === null || closeBtn === void 0 ? void 0 : closeBtn.addEventListener('click', () => {
    nav.classList.remove('open');
});
console.log('end of script');
