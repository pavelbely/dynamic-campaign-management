{
    id: 'accountId1',
    firstName: 'Sergey',
    lastName: 'Brin',
    contacts: [
        {
            contactId: 'c01',
            channel: 'email',
            value: 'sergey@gmail.com',
            status: 'valid'
        },
        {
            contactId: 'c02',
            channel: 'email',
            value: 'sergey@mail.ru',
            status: 'unverifyable'
        },
        {
            contactId: 'c03',
            channel: 'email',
            value: 'sergey@yahoo.com',
            status: 'invalid'
        },
        {
            contactId: 'c04',
            channel: 'email',
            value: 'sergey@mail.co.il',
            status: 'unknown'
        },
        {
            contactId: 'c05',
            channel: 'phone',
            value: '1234567890',
            status: 'valid'
        },
        {
            contactId: 'c06',
            channel: 'phone',
            value: '99999999999',
            status: 'unverifyable'
        },
        {
            contactId: 'c07',
            channel: 'phone',
            value: '222222222',
            status: 'invalid'
        },
        {
            contactId: 'c08',
            channel: 'phone'
            value: '33333333333',
            status: 'unknown'
        },
        {
            contactId: 'c09',
            channel: 'linkedin',
            value: 'linkedin.com/sergeybrin',
        },
        {
            contactId: 'c10',
            channel: 'angellist',
            value: 'angel.co/sergeybrin',
        },
    ],
    urls: [
        {
            type: 'blog',
            url: 'sergey.com',
        },
    ],
    currentPosition: { 
        name: 'Software Engineer',
        company: 'googleCompanyId',
        startedAt: date('2020-01-01'),
    },
    allPositions: [
        { # We're duplicating this so as to simplify MongoDB queries when finding past or current positions
            name: 'Software Engineer',
            company: 'googleCompanyId',
            startedAt: date('2020-01-01'),
        },
        {
            name: 'QA',
            company: 'microsoftCompanyId',
            startedAt: date('2019-01-01'),
            endedAt: date('2019-12-31'),
        },
    ],
    tags: ['metInPerson', 'campaignA', 'neverSendAmazonGiftCards'],
    location: {
        city: 'San Francisco',
        country: 'USA'
    }
}