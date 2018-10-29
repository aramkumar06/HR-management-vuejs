export default {
  items: [
    {
      title: true,
      name: 'Income Pages',
      wrapper: {            // optional wrapper object
        element: '',        // required valid HTML5 element tag
        attributes: {}        // optional valid JS object with JS API naming ex: { className: "my-class", style: { fontFamily: "Verdana" }, id: "my-id"}
      },
      class: ''             // optional class names space delimited list for title item ex: "text-center"
    },
    {
      name: 'My Income',
      url: '/MyEarning',
      icon: 'icon-user',
    },
    {
      name: 'Team Income',
      url: '/TeamEarning',
      icon: 'icon-people',
    },
    {
      name: 'Company Income',
      url: '/CompanyEarning',
      icon: 'icon-organization',
    },
    {
      title: true,
      name: 'Personal Info Pages',
      wrapper: {            
        element: '',        
        attributes: {}        
      },
      class: ''             
    },
    {
      name: 'Account Setting',
      url: '/AccountSetting',
      icon: 'icon-user-follow',
    },
    {
      name: 'My Contacts',
      url: '/MyContacts',
      icon: 'icon-credit-card',
    },
    {
      name: 'My Projects',
      url: '/MyProjects',
      icon: 'icon-layers',
    },
    {
      name: 'My Equips',
      url: '/MyEquips',
      icon: 'icon-screen-desktop',
    },
    {
      title: true,
      name: 'Admin Pages',
      wrapper: {            
        element: '',        
        attributes: {}        
      },
      class: ''             
    },
    {
      name: 'Manage Income',
      url: '/ManageIncome',
      icon: 'icon-diamond',
    },
    {
      name: 'Manage Projects',
      url: '/ManageProjects',
      icon: 'icon-layers',
    },
    {
      name: 'Manage Members',
      url: '/ManageMembers',
      icon: 'icon-people',
    },
    {
      name: 'Manage Accounts',
      url: '/theme/typography',
      icon: 'icon-user-follow',
    },
    {
      name: 'Manage Equip',
      url: '/theme/typography',
      icon: 'icon-screen-desktop',
    }
  ],
};
