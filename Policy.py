from tkinter import *
import tkinter as tk

class Policy(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1355x900+0+0")
        self.title('Policy')
        self.resizable(False,False)

        #frame
        self.top = Frame(self, height=150, bg='#e2eafc')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=900, bg='#e2eafc')
        self.bottom.pack(fill=X)

        #top frame design
        f1 = Frame(self.top, width=1360, height=100, bd=8, bg="#0b090a")
        f1.place(x=230, y=0)

        lbl_information = Label(f1, font=('arial', 45, 'bold'), text="ORGANISATIONAL POLICIES", relief=GROOVE, bd=10, bg="#0077b6", fg="White")
        lbl_information.grid(row=0, column=0)

        self.bottom2 = Frame(self.bottom, width=1350, height=900, bd=10, bg='White')
        self.bottom2.place(x=210, y=0)

        scroll_y = Scrollbar(self.bottom2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.policy = Text(self.bottom2, font=("TimesNewRoman", 15), bg="white", yscrollcommand=scroll_y.set)
        self.policy.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.policy.yview)

        #buttons
        self.Button1 = Button(self.bottom, text="    Late Coming Policy    ", font=("arial", 12, "bold"), bg='#0077b6', fg='White')
        self.Button1.place(x=5, y=0)

        self.Button2 = Button(self.bottom, text="           Leave Policy          ", command=self.leavepolicy, font=("arial", 12, "bold"), bg='#0077b6', fg='White')
        self.Button2.place(x=5, y=45)

        self.Button3 = Button(self.bottom, text="Code of Conduct Policy", font=("arial", 12, "bold"), bg='#0077b6', fg='White')
        self.Button3.place(x=5, y=90)

        self.Button4 = Button(self.bottom, text="      Attendance Policy     ", font=("arial", 12, "bold"), bg='#0077b6', fg='White')
        self.Button4.place(x=5, y=135)

    def leavepolicy(self):
        #label1
        label1 = Label(self.bottom2, font=('arial', 20, 'bold'), text="Leave Policy", bg="#ffffff", fg="#ef233c")
        label1.place(x=20, y=20)

        #content
        text1 = Text(self.bottom2, height=28, width=100)
        scroll = tk.Scrollbar(self.bottom2, command=text1.yview)
        text1.configure(yscrollcommand=scroll.set)
        text1.tag_configure('bold', font=('Arial', 12, 'bold'))
        text1.tag_configure('big', font=('Arial', 12, 'bold'))
        text1.tag_configure('color', foreground='black', font=('Arial', 12, 'bold'))

        quote = """
        Leave means “To go away for something for a short time”. An employee is suppose to fulfill both professional and 
        personal commitment so one is suppose to take short time duration off to fulfill personal commitment and such offs 
        must be duly approved by reporting manager then only an employee  proceed further. Now this question also originate 
        in the mind that why do we need to have leave policy for employees.
        
        -- Why Leave Policy?

        People are the most valuable asset of an organization. Lack of proper leave management can lead to unauthorized 
        absence of employees from duty, lower productivity, fall in productivity hours, missing of important targets and 
        so on. These types of issues can be resolved with a proper Leave Policy Manual for employees in workplace. For 
        instance if an employee is on leave with no prior information his/her work suffers as nobody is prepared for the 
        unexpected absence. But on similar terms if an employee applies for leave in advance in such case the stakeholder 
        are aware of it and the entire team can manage the work in employee absence so that there is no loss of productivity. 
        Leave Policy when implemented in the company it provides a common understanding between the employer and employee 
        that how leave can be taken while in service.

        Some advantages of having a Company HR Leave Policy in place are: This HR Leave policy sample exerts on the fact 
        that each service need to have policies which can help them guide to prepare for unexpected.

            1. Having the right leave policy, it satisfies the legal obligation and safety.
            2. It helps in better relationship between the employer and the employee.
            3. It provides for more flexible time off.
            4. It ensures to avoid any kind of ambiguity how particular situation should be handled.

        In the below policy we will get to know what are various types of leave. What are the guidelines to be followed 
        for availing leave? Under what circumstances employee can avail casual leave, earned leave, unpaid leave, 
        maternity leave, paternity leave. What is leave of absence policy? What are Paid and Unpaid Leave? When can 
        an employee take Leave with pay or Leave without pay. These details have been covered in Leave policy sample below.

        Disclaimer: The content prepared has been created with greatest care. These policies have been prepared for sample. 
        However for accuracy and completeness hrhelpboard.com cannot guarantee. The user is therefore requested to professionally 
        check the suitability of all content for its use.

        Objective: The objective of the Leave Policy is to give provision to the employees to balance their personal as well 
        as professional life. This Compnay HR Leave Policy sample is also meant to fulfill the statutory requirement regarding 
        leave and holidays.

        -- Sample Compnay HR Leave Policy for Employees 

            Purpose: The purpose of leave policy for employees is to lay guidelines regarding when to avail leave and the 
            process to take leave with pay, leave without pay, Leave of absence policy and so on.

            Eligibility: The Leave policy is applicable to all the regular employees of the company.

        -- Guidelines for Leave Policy: - A Company HR Leave Policy for Employees
        
            1. Leave cannot be claimed as a matter of right. Any kind of leave can be granted or refused depending upon the 
            business demands. Leave of absence from work without proper approval will call for disciplinary action. Leave meaning 
            is to go away for something for a short period of time.
            2. The calendar year for leave is from January to December.
            3. All leave record of the employees shall be maintained in HRMS tool.
            4. All leaves should be applied on HRMS tool before proceeding on leave. In case of emergency when leave cannot be applied 
            in advance, telephonic intimation to the immediate reporting manager should be done and it must be regularized within 2 days 
            of resuming duty on HRMS tool.
            5. Leaves will be credited to employees account in the beginning of calendar year i.e. January. Earned Leave will be 
            updated on a monthly basis for the leave earned during the month. It will be credited at the rate of 1.75 leave per 
            month. For existing employees carried forward earned leave balance from previous year will be updated in the month of January.
            6. Employees will be eligible for Earned Leave only after completion of probationary period. On confirmation Earned leave for 
            the period of probation will be credited to employees account.
            7. It is mandatory for an employee to utilize 18 leaves during an year. It should be 12 EL and 6 CL. It is meant to fulfill the 
            objective of maintaining the work life balance.
            8. A Maximum of 9 earned leave can be carried forward to next year.
            9. Employee may apply for leave depending upon their leave balance available to their credit on HRMS tool.
            10. An employee can avail paid leave depending upon the leave balance available to employee also unpaid leave can be availed 
            when leave balance is exhausted and employee is in need of leave on approval from immediate manager, HOD and HR.
            11. Employees joining during course of year shall be subject to receive Leave on pro-rata basis in their leave account on HRMS tool.
            12. An employee shall not proceed on leave until unless leave has been approved by reporting manager.
            13. If an employee is absent continuously for 7 days beyond sanctioned leave with no information, in this case employee 
            shall be considered to have left his/her employment on one’s free will. HR will take action in this case. First Warning letter 
            will be issued to the employee if he/she does not return within 7 days of expiry of sanctioned leave. If no response from 
            employee within 3 days of issuance of 1st warning letter, 2nd warning letter will be issued. If there is still no response from 
            the said employee final termination letter will be issued in 3 days after issuance of 2nd warning letter.
            14. In case of prolonged illness or leave of absence from work an employee is suppose to inform the immediate reporting 
            manager at regular interval about their condition and most probable date of return. In absence of any communication from 
            employee serious action can be taken by the company.
            15. Leave without approval will be considered as leave without pay.
            16. Weekends and any holiday lying between the sanctioned leave periods will be excluded and not be counted as leave in 
            case of casual and earned leave.
            17. Leave for coming year cannot be availed in the current year.
            18. In case of planned leave it is employee responsibility to apply for leave in advance, however in case of unplanned leave 
            employee must regularize leave within 2 days of resuming duty.
            19. Leave for the purpose of LTA should be earned leave. It cannot be casual

        -- Types of Leave

        There are different types of Leaves given and listed in Company HR Annual Leave Policy. The leaves can be categorized as 
        Annual Paid Leave or Unpaid Leave. Some leave which are approved and granted to an employee basis availability of 
        leave balance are paid leave or leave with pay.

        However unpaid leave or leave without pay can be availed by an employee at the time of emergency and when no leave balance left.

        1. Casual Leave
        2. Earned leave
        3. Maternity Leave
        4. Paternity Leave
        5. Leave without pay
        6. Compensatory off

        1. Casual Leave
            
            1. Maximum 12 days of casual leave can be availed by an employee in a year.
            2. Casual leave is paid leave.
            3. Employee joining during the course of year will be entitled for casual leave on pro-rata basis.
            4. Casual leave can be taken for minimum half day and maximum 4 days.
            5. Leave for more than 4 days can be taken as earned leave.
            6. Casual leave cannot be carried forward to next year.
            7. Casual leave cannot be clubbed with earned leave or any other type of leave.
            8. Casual leave should be applied one day in advance and a week in advance when it is applied for more than 2 days.
            9. Casual leave not availed during the year will lapse at the end of year.

        -- Process for Casual Leave

            Casual leave applied by an employee on HRMS tool. For approval the leave notification will reach the immediate 
            reporting manager. Once approved, approval notification will reach to employee and HR. Leave are deducted from 
            leave balance from the employees account and latest balance updated on HRMS tool

        2. Earned Leave

            1. Leave application for Earned leave must reach reporting manager 15 days in advance.
            2. For new joiners joining during the mid of year privilege leave will be credited on pro rata basis.
            3. For existing employees leaves will be credited in the beginning of the year, entitlement however will be 
            based on number of months worked. For every month completed 1.75 of privilege leave will be credited to 
            employees account.
            4. Privilege leave can be carried forward to next year up to a maximum of 9 days. However for existing employees
            who are into service for more than 5 years a maximum of 45 days can be carried forward. Leave above 45 days 
            will lapse automatically.
            5. Employees who have resigned from their duties privilege leave entitlement would be calculated on pro rata 
            basis till their last working day.
            6. For the calculation of LTA, 5 days leave are compulsory to be availed by an employee (inclusive of holidays).

        -- Process for Earned Leave

            Employee must apply for earned leave 15 days in advance. Once applied, notification will reach immediate 
            reporting manager. Once approved leave notification will reach employee and HR. Leave balance after deduction 
            will be updated on HRMS     

        3. Maternity Leave

            1. All confirmed female employees shall be entitled for Maternity leave as per maternity benefit act 2016, 
            with full pay for a period of continuous 26 weeks (excluding national holidays) for each pregnancy up 
            to a maximum of 2 confinements.
            2. Leave taken for prenatal treatment for the first 7 months of pregnancy will be considered as normal 
            leave not maternity leave.
            3. A woman employee can take maternity leave earliest 8 weeks before the expected date of delivery.     
        
        -- Process of Maternity Leave

            Before preceding on Maternity Leave it is needed to be applied on HRMS tool and must be approved by the reporting manager.
            The woman employee proceeding on Maternity leave must also submit doctor’s certificate to HR.
            
        -- Leave in case of adoption of child or birth through surrogacy 

            In case of adoption of child or child birth through surrogacy a woman employee is entitled for 12 weeks of leave.
            These Leaves can be availed on when the child has actually started living with the parents

        -- Process of leave in case of adoption of child or child birth through surrogacy

            In the above mentioned case leave must be applied at least 6 weeks before the date of adoption.
            All legal certificate and required documents must be submitted to HR.
        
        4. Paternity Leave

            1. All regular male employees are eligible for paternity leave.
            2. A maximum of 7 days of paternity leave can be availed by an employee.
            3. The paternity leave must be taken within 15 days of child birth, failing which the leaves will lapse.
            4. The leave must be taken at a stretch.
            5. In case of adoption or surrogacy leave can be taken only if child is actually living with the parents

        -- Process of Paternity leave

            Paternity leave must be applied at least 15 days before the expected date of delivery.
            Employee can commence for leave from the actual date of delivery.
            The leave must be approved by immediate reporting manager.

        5. Leave without pay
            
            1. An employee can avail leave without pay in case existing leave balance is exhausted and employee is in 
            need of leave due to unforeseen circumstances.
            2. In case no approval taken for leave without pay, such absence of employee will be considered as Leave 
            of absence from work.
            3. Disciplinary action will be taken in case of absence without approval.
            4. No salary would be given to employee for the days leave without pay is availed.
            5. A maximum of 3 months of leave without pay can be availed by an employee.
            6. Loss of pay can be availed by an employee by applying on HRMS tool for approval from immediate reporting 
            manager and head of department.
            7. Once approved by immediate reporting manager and department head, Leave can be availed by employee.
            8. Leave will be updated as loss of pay on HRMS tool. 

        -- Process for availing leave without pay

            Loss of Pay can be availed by an employee by applying on HRMS tool for approval from immediate reporting 
            manager and head of department.
            Once approved by immediate reporting manager and department head, leave can be availed by employee.
            Leave will be updated as loss of pay on HRMS tool.
        
        6. Compensatory off

            1. An employee is eligible for compensatory off when he/she has worked on an important assignment on any of the 
            national/festival/declared off day.
            2. Approval to work on any such day i.e. national/festival/declared off day must be taken by senior management
            3. Compensatory off must be availed within a period of 1 month else it will lapse.

        -- Process to avail compensatory loss

            Approval of senior management is must for compensatory off. Employee who has worked on national/festival/declared 
            off day can avail leave in lieu of work done on above mentioned days. The day employee is taking compensatory off 
            he/she must inform immediate reporting manager, once approved, it is immediate managers responsibility to 
            inform HR about the same. 

            Leave of absence policy:  The leave of absence policy is defined as an unpaid duly approved absence from work 
            for a limited period of time for medical or personal reasons. 

        -- Process of leave of absence policy:

            Medical reasons: A request for leave of absence from work must be raised on HRMS tool. The request will reach 
            the immediate supervisor and Head of department for approval. An employee is supposed to take approval from 
            Leave of absence from work at least 20 days in advance when the need for leave is foreseeable. In case of 
            leave of absence from work due to medical reasons a certificate from physician need to be submitted to HR.

            Personal reason: An employee can apply for Leave of absence from work when in need due to some unforeseen 
            reasons. The maximum days of leave of absence  can be applied for six weeks

        -- Cancellation of leave

            1. Approved leave can be cancelled depending upon the business demand.
            2. Leave once cancelled by reporting manager an automatic notification will reach to the employee and the HR.
            3. Leave balance will be updated accordingly by HR

        -- Extension of leave

            1. In case of extension of leave due to any unforeseen circumstances the employee must inform reporting manager in advance; 
            once extension of leave is approved by reporting manager it is manager’s duty to inform HR. This is the case when leave 
            extension has been told verbally or over the phone. It is employee responsibility to regularize leave on HRMS tool once employee 
            has resumed back on duty.
            2. The extended leave must be applied on HRMS tool in case of planned extension so that both the reporting manager and HR 
            are informed automatically.
            3. Leave balance is updated on HRMS tool by HR.
            4. In case employee overstays without approval it will be treated as absence from duty and disciplinary 
            action will be taken against the employee.
            5. Leave extended without permission will be treated as loss of pay    

        -- Leave calculation on resignation/termination

            In case employee has resigned from the services or on termination of employee privilege leave will be calculated 
            till the last working day of the employee and will be paid in full and final settlement of the employee

        -- Revision of the policy

            The company reserves the right to revise, modify any or all clauses of this policy depending upon demand of business.

        -- Explanation of Leave policy

            Corporate HR department will be sole authority to interpret the content of this policy.
        
        """
        text1.insert(END, quote, 'color')
        text1.place(x=20, y=70)
